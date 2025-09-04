# Commix-Automation-
Commix Script for autionation for CTF
# Commix Automation Framework for CTFs & Labs

⚠️ **WARNING:** This tool is intended **only for educational purposes, Capture The Flag (CTF) challenges, and lab environments**.  
Do **NOT** use this tool against unauthorized websites or networks. The author is not responsible for any illegal activity or damage caused by misuse.

---

## Overview

This is an **interactive, professional-grade automation framework for Commix**, designed to:

- Automate **OS command injection testing** in web applications  
- Bypass basic **WAF protections** using tamper scripts  
- Support multiple **injection vectors** (GET, POST, cookies, headers)  
- Cycle through **classic, blind, and time-based techniques**  
- Execute **optional shell commands** for enumeration  
- Instantly detect and print **flags** for CTFs  
- Handle **multiple targets** in batch mode  

This framework is **optimized for CTF competitions** and lab pentests, giving you fast, flexible control over Commix payloads and techniques.

---

## Features

| Feature | Description |
|---------|-------------|
| Multi-target support | Test multiple URLs from a list automatically |
| Injection vectors | GET, POST, Cookie, Header |
| WAF bypass | Built-in tamper chaining (`space2comment`, `percent20`, `semicolon2newline`, `lowercase`) |
| Techniques | Classic, blind, time-based |
| Shell commands | Optional system enumeration (`id`, `whoami`, etc.) |
| Flag detection | Prints lines containing CTF flags instantly |
| Timeout handling | Prevents script from hanging on slow targets |
| Interactive menu | Choose targets, vectors, tamper scripts, techniques, and shell commands dynamically |

---

## Installation

1. Clone the repository:
```bash   
git clone https://github.com/yourusername/commix-automation.git
cd commix-automation
```

2. Ensure Commix is installed and accessible:
````bash
git clone https://github.com/commixproject/commix.git

````

4. Install Python 3 if not already installed.

---

Usage

Prepare your targets list

Create a file named targets.txt with one URL per line:

http://example.com/vuln.php?id=1
http://example.com/test.php?cmd=

Run the interactive menu version
```
python3 commix_interactive.py

```
Select injection vectors, tamper scripts, techniques, and shell commands from the terminal menu

Flags and shell outputs are printed instantly


Run the speed-mode batch version

python3 commix_speed_ctf.py

Automatically loops through targets

Uses tamper chaining and multiple techniques

Prints flags and optional shell command results immediately



---

Configuration Options

COMMIX_PATH – Path to your commix.py

FLAG_KEYWORD – Keyword used to identify flags (default: FLAG{)

SHELL_COMMANDS – Optional commands for enumeration

TAMPERS – List of tamper scripts for WAF bypass

TECHNIQUES – Command injection techniques (classic, blind, time-based)

EXTRA_HEADERS – Optional HTTP headers for bypass

COOKIES – Optional cookie injection



---

Legal & Safety Disclaimer

Only use this tool in environments you own or are authorized to test

Do not run this against live production websites without permission

Use responsibly in labs, CTFs, or controlled testing environments

Misuse can lead to legal consequences


---

References & Resources

Commix Official Repository

OWASP Command Injection

CTF platforms: HackTheBox, TryHackMe, PicoCTF



---

License

This project is open-source and released under the MIT License.
Educational use only. No warranty or liability.
