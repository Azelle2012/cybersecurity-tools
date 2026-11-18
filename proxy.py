import socket
import re

HOST, PORT = '127.0.0.1', 8080

def iniciar():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server.bind((HOST, PORT))
    server.listen(5)
    print(f"[*] Proxy en {HOST}:{PORT}")
    while True:
        client, addr = server.accept()
        req = client.recv(8192)
        if not req: continue
        text = req.decode('utf-8', errors='ignore')
        host_match = re.search(r"Host: (.*?)\r\n", text)
        if not host_match:
            client.close(); continue
        target = host_match.group(1).strip()
        modified = re.sub(r"User-Agent: .*?\r\n", "User-Agent: Mozilla/5.0 (iPhone)\r\n", text)
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((target, 80))
            s.send(modified.encode())
            resp = s.recv(8192)
            client.send(resp)
            s.close()
        except Exception as e:
            print(f"Error: {e}")
        client.close()

if __name__ == "__main__":
    iniciar()