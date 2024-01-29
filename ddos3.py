import socket
import threading

target_ip = "127.0.0.1"
target_port = 80

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

sock.connect((target_ip, target_port))

def send_data():
    while True:
        sock.send(b"A" * 1024)
thread = threading.Thread(target=send_data)
thread.start()

while True:
    pass
