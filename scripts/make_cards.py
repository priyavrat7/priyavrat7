#!/usr/bin/env python3
"""Draw the GitHub stats and top-languages cards shown on the profile README.

Counts PUBLIC activity only: private repositories are filtered out even if the
token can see them. Needs GITHUB_TOKEN (provided automatically in GitHub Actions).
"""
import json, os, pathlib, sys, urllib.request
from html import escape

USER = "priyavrat7"
NAME = "Priyavrat Sharma"
OUT = pathlib.Path(__file__).resolve().parent.parent / "assets"
FONT = "'Segoe UI', Ubuntu, Helvetica, Arial, sans-serif"

QUERY = """
query($login: String!, $prs: String!, $issues: String!, $cursor: String) {
  prs: search(query: $prs, type: ISSUE) { issueCount }
  issues: search(query: $issues, type: ISSUE) { issueCount }
  user(login: $login) {
    contributionsCollection {
      commitContributionsByRepository(maxRepositories: 100) { repository { nameWithOwner isPrivate } contributions { totalCount } }
      issueContributionsByRepository(maxRepositories: 100) { repository { nameWithOwner isPrivate } }
      pullRequestContributionsByRepository(maxRepositories: 100) { repository { nameWithOwner isPrivate } }
      pullRequestReviewContributionsByRepository(maxRepositories: 100) { repository { nameWithOwner isPrivate } }
    }
    repositories(first: 100, after: $cursor, ownerAffiliations: OWNER, privacy: PUBLIC) {
      pageInfo { hasNextPage endCursor }
      nodes {
        isFork
        stargazerCount
        languages(first: 20, orderBy: {field: SIZE, direction: DESC}) { edges { size node { name color } } }
      }
    }
  }
}
"""


def fetch(cursor=None):
    token = os.environ.get("GITHUB_TOKEN")
    if not token:
        sys.exit("GITHUB_TOKEN is not set")
    body = {"query": QUERY, "variables": {
        "login": USER, "cursor": cursor,
        "prs": f"author:{USER} is:pr is:public",
        "issues": f"author:{USER} is:issue is:public"}}
    req = urllib.request.Request("https://api.github.com/graphql", data=json.dumps(body).encode(),
                                 headers={"Authorization": f"Bearer {token}", "User-Agent": "profile-cards"})
    with urllib.request.urlopen(req, timeout=60) as r:
        data = json.load(r)
    if data.get("errors"):
        sys.exit(f"GraphQL error: {data['errors']}")     # fail loudly, keep the old cards
    return data["data"]


def collect():
    data = fetch()
    cc = data["user"]["contributionsCollection"]
    commits = sum(x["contributions"]["totalCount"]
                  for x in cc["commitContributionsByRepository"] if not x["repository"]["isPrivate"])
    contributed = {x["repository"]["nameWithOwner"]
                   for group in cc.values() for x in group
                   if not x["repository"]["isPrivate"]
                   and not x["repository"]["nameWithOwner"].lower().startswith(USER.lower() + "/")}
    repos, page = [], data["user"]["repositories"]
    while True:
        repos += page["nodes"]
        if not page["pageInfo"]["hasNextPage"]:
            break
        page = fetch(page["pageInfo"]["endCursor"])["user"]["repositories"]
    own = [r for r in repos if not r["isFork"]]
    langs = {}
    for r in own:
        for e in r["languages"]["edges"]:
            name = e["node"]["name"]
            size, color = langs.get(name, (0, e["node"]["color"] or "#8b949e"))
            langs[name] = (size + e["size"], color)
    stats = [("Total Stars Earned", sum(r["stargazerCount"] for r in own)),
             ("Total Commits (last year)", commits),
             ("Total PRs", data["prs"]["issueCount"]),
             ("Total Issues", data["issues"]["issueCount"]),
             ("Contributed to (last year)", len(contributed))]
    return stats, sorted(langs.items(), key=lambda kv: -kv[1][0])[:6]


def card(width, title, inner):
    return (f'<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="195" viewBox="0 0 {width} 195" role="img" aria-label="{escape(title)}">\n'
            f'<rect width="{width}" height="195" rx="6" fill="#151515"/>\n'
            f'<g font-family="{FONT}">\n'
            f'<text x="25" y="36" font-size="18" font-weight="600" fill="#ffffff">{escape(title)}</text>\n'
            f'{inner}</g>\n</svg>\n')


def stats_card(stats):
    rows = "".join(
        f'<text x="25" y="{70 + i * 25}" font-size="14" font-weight="600" fill="#9f9f9f">{escape(label)}:</text>'
        f'<text x="300" y="{70 + i * 25}" font-size="14" font-weight="700" fill="#ffffff">{value}</text>\n'
        for i, (label, value) in enumerate(stats))
    return card(390, f"{NAME}'s GitHub Stats", rows)


def langs_card(langs):
    total = sum(size for _, (size, _c) in langs) or 1
    bar, legend, x = "", "", 25.0
    for i, (name, (size, color)) in enumerate(langs):
        w = 300 * size / total
        bar += f'<rect x="{x:.2f}" y="55" width="{w:.2f}" height="8" fill="{color}"/>'
        x += w
        col, row = i // 3, i % 3
        cx, cy = 30 + col * 155, 95 + row * 28
        legend += (f'<circle cx="{cx}" cy="{cy - 4}" r="5" fill="{color}"/>'
                   f'<text x="{cx + 12}" y="{cy}" font-size="12" fill="#9f9f9f">{escape(name)} {100 * size / total:.2f}%</text>\n')
    clip = '<clipPath id="bar"><rect x="25" y="55" width="300" height="8" rx="4"/></clipPath>'
    return card(350, "Most Used Languages", f'{clip}<g clip-path="url(#bar)">{bar}</g>\n{legend}')


def main():
    stats, langs = collect()
    OUT.mkdir(exist_ok=True)
    (OUT / "stats.svg").write_text(stats_card(stats))
    (OUT / "languages.svg").write_text(langs_card(langs))
    print(dict(stats))
    print([(n, s) for n, (s, _) in langs])


if __name__ == "__main__":
    main()
