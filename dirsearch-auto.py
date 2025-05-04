import subprocess
import time

def fuzz_domains(file_path):
    try:
        with open(file_path, 'r') as f:
            domains = [line.strip() for line in f if line.strip()]

        for domain in domains:
            print(f"\n[+] Fuzzing: {domain}")
            try:
                subprocess.run(["dirsearch", "-u", domain])
                print(f"[✓] Done: {domain}")
            except Exception as e:
                print(f"[!] Error on {domain}: {e}")

            time.sleep(1)  # optional delay between runs

    except FileNotFoundError:
        print(f"[!] File not found: {file_path}")
    except Exception as e:
        print(f"[!] Unexpected error: {e}")

if __name__ == "__main__":
    file_path = input("Enter the path to your domain list file: ").strip()
    fuzz_domains(file_path)
