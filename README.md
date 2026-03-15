# Python Network Scanner

A Python-based network scanning tool that identifies open ports on a target machine by attempting TCP connections across common port ranges. This project demonstrates fundamental network security concepts such as port scanning, service discovery, and host enumeration.

---

## Features

- Scans a target host for open TCP ports
- Detects exposed network services
- Command-line interface for specifying scan targets
- Uses Python sockets to establish connections
- Lightweight and easy to run

---

## Technologies Used

- Python
- Socket Programming
- TCP Networking
- Command Line Interface (argparse)

---

## Project Structure

```
network-scanner
│
├── scanner.py
└── README.md
```

---

## Installation

Clone the repository:

```
git clone https://github.com/YOURUSERNAME/network-scanner.git
```

Navigate into the project directory:

```
cd network-scanner
```

---

## Usage

Run the scanner and provide a target IP address:

```
python scanner.py 127.0.0.1
```

Example output:

```
Scanning target 127.0.0.1

Port 22 is OPEN
Port 80 is OPEN
Port 443 is OPEN
```

---

## Security Concept

Port scanning is a common reconnaissance technique used in cybersecurity to identify open ports and exposed services on a host. Open ports may indicate running services that could be vulnerable to attack if misconfigured or outdated.

This tool demonstrates the basic mechanics of how scanners like **Nmap** detect open services on a network.

---

## Future Improvements

- Multithreaded scanning for faster results
- Service detection (identify HTTP, SSH, etc.)
- IP range scanning (subnet scanning)
- Export scan results to a report file

---

## Author

Kaysen Acfalle
