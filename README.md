# mini-soc-log-analysis
Mini SOC project to detect suspicious login attempts
# Mini SOC Log Analysis Project

![Domain](https://img.shields.io/badge/Domain-SOC%20Operations-blue)
![Project](https://img.shields.io/badge/Focus-Log%20Analysis-purple)
![Status](https://img.shields.io/badge/Status-Completed-success)

---

Objective

To analyze login logs and detect suspicious IP addresses based on repeated failed login attempts using Python.

---

Log Format

Each log entry contains:
Timestamp | Status | IP Address

Example:
2026-01-01 LOGIN FAILED 192.168.1.10

---

Detection Logic

* Identify "FAILED" login attempts
* Count number of failures per IP
* Flag IPs with 3 or more failed attempts

---

Output Example

Suspicious IP: 192.168.1.10

---

Project Files

* login-logs.txt
* suspicious-ip-detector.py

---

How to Run

1. Open terminal in project folder
2. Run:
   python suspicious-ip-detector.py

---

SOC Insights

* Detects potential brute-force attack patterns
* Helps identify suspicious login behavior

---

Skills Demonstrated

* Log Analysis
* Python Scripting
* Basic Threat Detection
* Problem Solving
