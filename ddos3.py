import requests
import time

def visit_website(url, num_visits):
    for _ in range(num_visits):
        response = requests.get(url)
        print(f"Visited {url} - Status Code: {response.status_code}")
        time.sleep(0)

if __name__ == "__main__":
    website_url = input("Enter the website URL to visit: ")
    num_visits = int(input("Enter the number of visits: "))

    visit_website(website_url, num_visits)
