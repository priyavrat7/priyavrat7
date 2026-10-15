<h1 align="center">Priyavrat Dev Sharma</h1>

<p align="center">
Software Developer, Networking and Distributed Systems, Applied ML<br/>
MSc Electrical and Computer Engineering, McGill University
</p>

<p align="center">
<a href="https://priyavrat7.github.io/MyGitPage/index.html"><img src="https://img.shields.io/badge/Portfolio-0A66C2?style=for-the-badge&logo=googlechrome&logoColor=white" /></a>
<a href="https://www.linkedin.com/in/priyavrat-sharma-537b6113a/"><img src="https://img.shields.io/badge/LinkedIn-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white" /></a>
<a href="mailto:priyavrat.sharma@mail.mcgill.ca"><img src="https://img.shields.io/badge/Email-D14836?style=for-the-badge&logo=gmail&logoColor=white" /></a>
<a href="https://ieeexplore.ieee.org/document/11162378"><img src="https://img.shields.io/badge/IEEE%20Publication-00629B?style=for-the-badge&logo=ieee&logoColor=white" /></a>
</p>

---

### About

I am a Research Software Developer at the McGill Centre for Integrative Neuroscience (MCIN), where I work on [LORIS](https://github.com/aces/Loris), an open source platform for neuroimaging and clinical research data. My day to day mixes PHP, MySQL, React and Linux, with release testing, SQL migrations and access control review on the side. Networking is the thread through the rest of my work, see the section below.

Before that I completed an MSc in Electrical and Computer Engineering at McGill (CGPA 3.77/4.0, Graduate Excellence Award). My thesis and my [IEEE ICC 2025](https://ieeexplore.ieee.org/document/11162378) paper study routing for collaborative UAV networks. I also interned as a Machine Learning Engineer at Ericsson and spent three years as an embedded and software engineer at Jaipur Medical System.

Based in Montreal, Canada. I taught or assisted more than 700 students in Java, C++, Python, networking, machine learning and IoT courses.

---

### Networking

- **Research:** my thesis and [IEEE ICC 2025](https://ieeexplore.ieee.org/document/11162378) paper design multi hop routing for collaborative UAV networks. I modeled it as an integer linear program (IBM CPLEX) and wrote a modified Dijkstra heuristic in C++ that runs at least 99% faster than the exact solver, within 14% of optimal in the best configuration.
- **Protocols and simulation:** compared AODV, DSDV and DSR in the NS2 simulator with TCL scripts, looking at packet delivery ratio, convergence time and routing table behavior.
- **Fundamentals:** TCP/IP, UDP, ARP, OSPF, BGP, VLANs, L2 and L3 switching, SNMP and syslog. I taught networking fundamentals as a teaching assistant at McGill.
- **Tools:** Wireshark, tshark, tcpdump, nmap, Scapy, iperf3, mtr, hping, netstat, netcat, ping, traceroute and Cisco Packet Tracer.
- **Network automation:** open source contributions to Cisco pyATS and Genie (`genielibs`), the Meraki Dashboard API Python library and the Cisco AI Defense Python SDK, plus pyATS testbed and job files for test automation. Details are in the Open Source table below.
- **IoT networking:** MQTT and HTTP device protocols (smart home capstone), BLE 5.2 GATT firmware on the EFR32BG22, and MQTT telemetry from STM32 plant monitors.

---

### Experience

**Research Software Developer, MCIN (McGill Centre for Integrative Neuroscience)** | Feb 2026 to present
- Build and fix features in LORIS and its CBIG project fork: React replacements for legacy jQuery screens, instrument forms, user account pages, imaging upload and media error handling.
- Write idempotent SQL patches to create research projects and cohorts, and work on a foreign key aware candidate data deletion script.
- Reviewed role based access and session handling, which led to two security advisories that I reported and that are credited to me.
- Run release testing for LORIS 29.0 across 15+ modules and file the defects with reproduction steps.
- Designing an account request spam filter with a blocklist table and admin controls.

**Machine Learning Engineer, Ericsson Montreal Experience Studio** | May 2025 to Aug 2025
- Built a distributed training setup with PyTorch DDP on the Gloo backend, with checkpoint recovery and I2C hardware telemetry on every node.
- Wrote a Django control plane and REST API that orchestrates a virtual machine cluster, with Redis backed progress sharing and a live visualization.
- Worked on a Kafka and Redis image streaming pipeline across edge devices (Jetson Nano and Raspberry Pi) with automated tests in CI/CD.

**Research and Teaching Assistant, Advanced Networking Research Laboratory, McGill University** | Sept 2022 to Aug 2025
- Thesis: a C++ heuristic for multi source, multi destination routing in UAV networks, formulated against an exact integer linear program solved with IBM CPLEX. The heuristic ran at least 99% faster than CPLEX and came as close as 14% to optimal in the best configuration.
- Compared AODV, DSDV and DSR routing in the NS2 simulator using TCL scripts.
- Built a Spring Boot REST API for simulated UAV telemetry covering 50+ drones.
- Supported 700+ students through code review, debugging and lab sessions.

**Embedded Engineer (Software), Jaipur Medical System** | Jul 2019 to Jun 2022
- Built a document management platform with Spring Boot, PostgreSQL, Elasticsearch, JWT based access control and Docker.
- Wrote STM32 FreeRTOS firmware for oxygen plant monitoring, with interrupt driven sensing, interlock logic and MQTT telemetry, running at 95% uptime.
- Trained a model on historical specifications to predict project acceptance, which improved decision efficiency by 25%.

---

### Open Source

| Project | Contribution |
|---|---|
| [LORIS](https://github.com/aces/Loris) and its CBIG fork | 20 merged pull requests (14 in the fork, 6 in LORIS core), 30+ issues authored, two credited security advisories reported, review comments on other contributors pull requests |
| [genielibs](https://github.com/CiscoTestAutomation/genielibs) | Merged `pyasn1` pin update for denial of service CVEs. An approved fix for an igmp vrf KeyError is awaiting a second review |
| [meraki/dashboard-api-python](https://github.com/meraki/dashboard-api-python) | Merged change that registers five missing API categories |
| [ai-defense-python-sdk](https://github.com/cisco-ai-defense/ai-defense-python-sdk) | Merged documentation link fix |
| [k8s-objectmatcher](https://github.com/cisco-open/k8s-objectmatcher) | Approved fix for a StatefulSet volumeClaimTemplate diff bug, not yet merged |
| [HarmoniCA](https://github.com/julia-pfarr/HarmoniCA) | 4 merged pull requests: data harmonizer tab and CSV and Excel upload handling in a Python and Streamlit tool |

---

### Publication

**Optimizing Collaborative UAV (Drone) Networks for Data Efficiency in IoT Ecosystems**, IEEE ICC 2025 Workshops. [Read the paper](https://ieeexplore.ieee.org/document/11162378)

---

### Education

| Degree | Institution | Period |
|---|---|---|
| MSc, Electrical and Computer Engineering (Graduate Excellence Award) | McGill University, Canada | Sept 2022 to Aug 2025 |
| Post Graduate Certification, Internet of Things | BITS Pilani, India | Jul 2018 to Jun 2019 |
| BE, Electrical and Electronics | BIT Mesra, Ranchi, India | Jul 2013 to Jun 2017 |

---

### Skills

- **Languages:** Python, Java, C, C++, PHP, JavaScript, TypeScript, SQL, Bash
- **Web and backend:** React, Next.js, Spring Boot, Django, FastAPI, Flask, REST APIs
- **Data:** PostgreSQL, MySQL, MariaDB, MongoDB, Redis, Kafka, Elasticsearch
- **AI and ML:** PyTorch, scikit-learn, LangChain, Ollama, vLLM, embeddings and retrieval with ChromaDB and pgvector
- **Systems and cloud:** Linux, Docker, Kubernetes, Git, PhpStorm, GitHub Actions, AWS (S3, Lambda, DynamoDB)
- **Networking and embedded:** TCP/IP, UDP, ARP, OSPF, BGP, VLAN, SNMP, MQTT, BLE, Wireshark, tshark, tcpdump, nmap, Scapy, iperf3, Cisco Packet Tracer, NS2, pyATS, Genie, FreeRTOS, STM32, Raspberry Pi, Jetson Nano

---

### Selected Projects

| Project | Description |
|---|---|
| [Distributed Task Execution Framework](https://github.com/priyavrat7/Distributed-Task-Execution-Framework) | Team project in Java. Master worker system on Apache ZooKeeper with leader election, watchers and task reassignment |
| [Paxos Distributed Orders](https://github.com/priyavrat7/Paxos_Distributed_Orders) | Team project in Java. Paxos based total order broadcast with majority quorum and failure injection tests |
| [AI SaaS Prototype](https://github.com/priyavrat7/AI-SaaS-Prototype) | Job assessment prototype. Next.js and FastAPI with LangChain and OpenAI. A working vertical slice, not production software |
| [AI Medical App](https://github.com/priyavrat7/AI-at-the-Edge-of-Innovation) | Built with a team in a 24 hour TELUS hackathon. BLE sensor board, Android app and a FastAPI symptom matching service |
| [IoT Firmware for Health Monitoring](https://github.com/priyavrat7/IoT-Firmware-for-Health-Monitoring-System) | Embedded C for the Silicon Labs EFR32BG22 with BLE 5.2, I2C and SPI sensors and over the air updates |
| [Health Monitoring System](https://github.com/priyavrat7/Health-Monitoring-System) | Android app in Java with BLE sensors and a Firebase Firestore backend |
| [Stock Portfolio Manager](https://github.com/priyavrat7/Stock-Portfolio-Manager) | JavaFX desktop app with PostgreSQL over JDBC in Docker and live market data |

The [portfolio](https://priyavrat7.github.io/MyGitPage/projects.html) has the full list.

---

### Certifications

- [Internet of Things, BITS Pilani](https://drive.google.com/file/d/1X6Q8Iir_VT6OlRVYiaHYaCc7vX07QCUe/view?usp=drive_link)
- [Algorithmic Toolbox, University of California San Diego](https://www.coursera.org/account/accomplishments/verify/HECZZ86X9K9A)
- [Quebec Scientific Entrepreneurship Program, Fonds de recherche du Quebec](https://drive.google.com/file/d/1pF6cRxkK_4hsys-BbxB_pXOX-lYSbS-l/view)

---

<p align="center">
<img src="https://github-readme-stats.vercel.app/api?username=priyavrat7&theme=dark&hide_border=true&count_private=false" height="165"/>
<img src="https://github-readme-stats.vercel.app/api/top-langs/?username=priyavrat7&theme=dark&hide_border=true&layout=compact" height="165"/>
</p>
