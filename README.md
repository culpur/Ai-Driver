# AI Driver

An automated reconnaissance, exploitation, and AI-chained offensive security tool. Powered by OpenAI, Metasploit RPC, Burp/ZAP, and the full Kali Linux toolset.

---

## 🚀 Features

- **Layered Reconnaissance** using tools like `nmap`, `dig`, `subfinder`, `amass`, `whatweb`, `nikto`, `httpx`, and more.
- **AI-Suggested Actions** via OpenAI for chaining deeper recon or exploitation.
- **Automated Exploitation** using `ffuf`, `sqlmap`, `wpscan`, and Metasploit RPC.
- **Burp Suite / OWASP ZAP Integration** for passive and active web scans.
- **Report Generation** in both JSON and Markdown formats (with timeline and risk summary).
- **Modular Design** for extensibility and clean structure.

---

## 📁 Project Structure
ai_driver/
├── ai_driver.py               # Main orchestrator script
├── setup.sh                   # Environment setup script
├── README.md                  # This documentation
├── requirements.txt           # Python dependency list
├── modules/
│   ├── recon.py               # Layered recon logic
│   ├── exploitation.py        # FFUF, sqlmap, wpscan logic
│   ├── zap_burp.py            # Burp/ZAP API integrations
│   ├── metasploit.py          # Metasploit RPC automation
│   ├── ai_assistant.py        # AI suggestion engine
│   └── utils/
│       ├── logger.py          # Central logging utility
│       └── runner.py          # Safe shell command execution
└── targets/                   # Stores JSON/Markdown outputs per target

---

## ⚙️ Setup Instructions

git clone https://github.com/YOUR_ORG/ai_driver.git
cd ai_driver
bash setup.sh
source venv/bin/activate

---

## 🧠 Usage

ai_driver

Make sure .env is in JSON format, for example:

{
  "allow_exploitation": true,
  "scan_modes": [
    "port",
    "http",
    "dirbusting",
    "dns",
    "subdomain",
    "osint",
    "vulnscan"
  ],
  "target_scope": [
    "culpur.net"
  ],
  "max_runtime": 300,
  "max_threads": 10,
  "allowed_tools": [
    "nmap",
    "ffuf",
    "curl",
    "whois",
    "dig",
    "traceroute",
    "host",
    "dnsrecon",
    "theHarvester",
    "subfinder",
    "amass",
    "httprobe",
    "httpx",
    "whatweb",
    "nikto",
    "wafw00f",
    "shcheck",
    "wpscan",
    "aquatone",
    "masscan",
    "enum4linux-ng"
  ],
  "openai_api_key": "sk-proj-#########################"
}

⸻

📦 Dependencies

Listed in requirements.txt, includes:
	•	openai
	•	pymetasploit3
	•	requests
	•	python-dotenv
	•	aiofiles
	•	aiohttp
	•	msgpack
	•	httpx
	•	And more…

⸻

## 🔐 Legal

Use only against systems you are authorized to test. Unauthorized access is illegal.

⸻

## 👷 Contribution
	1.	Fork the repo
	2.	Make changes in feature branch
	3.	Submit PR

⸻

## 📜 License

MIT License © 2025 Culpur Defense Inc.
