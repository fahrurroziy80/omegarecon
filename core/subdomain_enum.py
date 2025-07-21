
import requests
import threading
from queue import Queue

COMMON_SUBDOMAINS = [
    "www", "mail", "ftp", "webmail", "smtp", "remote", "blog", "ns1", "ns2", "dev", "test"
]

def passive_sources(domain):
    try:
        url = f"https://crt.sh/?q=%25.{domain}&output=json"
        r = requests.get(url, timeout=10)
        if r.status_code == 200:
            data = r.json()
            return list(set([entry['name_value'] for entry in data if domain in entry['name_value']]))
    except Exception:
        pass
    return []

def brute_force(domain):
    found = []
    def worker():
        while True:
            sub = q.get()
            try:
                full = f"{sub}.{domain}"
                r = requests.get(f"http://{full}", timeout=2)
                found.append(full)
            except:
                pass
            q.task_done()

    q = Queue()
    for i in range(10):
        t = threading.Thread(target=worker)
        t.daemon = True
        t.start()

    for sub in COMMON_SUBDOMAINS:
        q.put(sub)

    q.join()
    return found

def enumerate(domain):
    passive = passive_sources(domain)
    brute = brute_force(domain)
    return list(set(passive + brute))
