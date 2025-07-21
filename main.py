
import argparse
from core import subdomain_enum
from utils.logger import log

def main():
    parser = argparse.ArgumentParser(description='OmegaRecon - Advanced Reconnaissance Tool')
    parser.add_argument('-d', '--domain', help='Target domain', required=True)
    parser.add_argument('--subs', help='Run subdomain enumeration', action='store_true')
    args = parser.parse_args()

    target = args.domain
    log(f"[+] Target: {target}")

    if args.subs:
        log("[*] Running Subdomain Enumeration...")
        found = subdomain_enum.enumerate(target)
        for sub in found:
            print(f"[+] {sub}")

if __name__ == '__main__':
    main()
