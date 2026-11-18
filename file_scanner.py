import sys
import requests

HEADERS = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"}
ARCHIVOS = [".env", ".git/config", "backup.zip", "config.php.bak", "robots.txt", "sitemap.xml", ".htaccess", "admin/", "wp-config.php.bak"]

def buscar(url_base):
    url_base = url_base.rstrip('/')
    print(f"[*] Buscando archivos en: {url_base}\n")
    for archivo in ARCHIVOS:
        url = f"{url_base}/{archivo}"
        try:
            r = requests.get(url, headers=HEADERS, timeout=5, allow_redirects=False)
            if r.status_code == 200:
                print(f"  [🔥] ENCONTRADO: {url} ({len(r.content)} B)")
            elif r.status_code == 403:
                print(f"  [🛡️] Protegido: {url}")
        except:
            pass

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Uso: python file_scanner.py <URL>")
        sys.exit(1)
    buscar(sys.argv[1])