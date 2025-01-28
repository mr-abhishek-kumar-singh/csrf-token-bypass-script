import requests
from bs4 import BeautifulSoup

def csrf_bypass(url, username, password):
    """
    Attempts to bypass CSRF token protection using a session-based POST request.

    Args:
        url (str): The URL of the login page.
        username (str): The username for authentication.
        password (str): The password for authentication.

    Returns:
        None
    """
    try:
        session = requests.Session()  # Creates a session for GET and POST requests

        # Step 1: Get CSRF token
        response = session.get(url)
        if response.status_code != 200:
            print(f"[!] Failed to connect to {url}. Status code: {response.status_code}")
            return
        
        soup = BeautifulSoup(response.text, "html.parser")  # Parses the HTML content
        csrf_token = soup.find("input", {"name": "csrf_token"})["value"]  # Extracts the CSRF token

        # Step 2: Use the token in the POST request
        data = {"username": username, "password": password, "csrf_token": csrf_token}
        response = session.post(url, data=data)

        # Step 3: Check the response
        if "Welcome" in response.text:
            print("[+] CSRF token bypass successful!")
        else:
            print("[!] CSRF token bypass failed.")
    except Exception as e:
        print(f"[!] An error occurred: {e}")

# User input for the target URL and credentials
url = input("Enter the URL of the login page: ")
username = input("Enter the username: ")
password = input("Enter the password: ")

csrf_bypass(url, username, password)
