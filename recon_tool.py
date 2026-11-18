import socket
import requests
import time

def escanear_puertos(host):
    print(f"\n[+] Escaneando {host}...")
    puertos = [21, 22, 23, 80, 443, 3306, 8080]
    for p in puertos:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(1)
        if s.connect_ex((host, p)) == 0:
            print(f"    Puerto {p} ABIERTO")
        s.close()

def obtener_cabeceras(url):
    print(f"\n[+] Cabeceras de {url}...")
    try:
        r = requests.get(url, headers={"User-Agent": "Mozilla/5.0"}, timeout=5)
        print(f"    Servidor: {r.headers.get('Server', 'No revelado')}")
        print(f"    Código: {r.status_code}")
    except Exception as e:
        print(f"    Error: {e}")

def fuzzing(url):
    print(f"\n[+] Fuzzing en {url}...")
    palabras = ["admin", "login", "backup", ".git", ".env", "config"]
    for p in palabras:
        try:
            r = requests.get(f"{url}/{p}", headers={"User-Agent": "Mozilla/5.0"}, timeout=3, allow_redirects=False)
            if r.status_code != 404:
                print(f"    [{r.status_code}] {url}/{p}")
        except:
            pass

while True:
    print("\n1. Puertos\n2. Cabeceras\n3. Fuzzing\n4. Salir")
    op = input("Opción: ")
    if op == "1":
        escanear_puertos(input("IP: "))
    elif op == "2":
        obtener_cabeceras(input("URL: "))
    elif op == "3":
        fuzzing(input("URL: "))
    elif op == "4":
        break