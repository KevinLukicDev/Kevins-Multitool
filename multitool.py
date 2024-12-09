import requests
import pyfiglet
from termcolor import colored
import random
import json
from datetime import datetime
import string
from urllib.parse import urlparse
import sys
from bs4 import BeautifulSoup

def ip_tracer():
    def save_to_json(ip_data):
        ip_data['timestamp'] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        
        try:
            with open('ip_history.json', 'r') as f:
                try:
                    history = json.load(f)
                except json.JSONDecodeError:
                    history = []
        except FileNotFoundError:
            history = []
        
        history.append(ip_data)
        
        with open('ip_history.json', 'w') as f:
            json.dump(history, f, indent=4)

    random_color = random.choice(["red", "green", "yellow", "blue", "magenta", "cyan", "white"])
    welcome = pyfiglet.figlet_format("IP-TRACER", font="slant")
    colored_welcome = colored(welcome, random_color)
    print(colored_welcome)

    print(colored("made by Kevin Lukic", "blue"))

    ip = input(colored("Enter an IP address: ", "yellow")).strip()
    
    # Basic IP validation
    if not ip or any(not (c.isdigit() or c == '.') for c in ip):
        print(colored("Invalid IP address format", "red"))
        return

    try:
        response = requests.get(f"https://ipinfo.io/{ip}/json", timeout=10)
        response.raise_for_status()
        
        data = response.json()
        required_fields = ['country', 'city', 'region', 'org', 'postal', 'timezone']
        
        for field in required_fields:
            value = data.get(field, 'Not available')
            print(colored(f"{field.capitalize()}: {value}", random_color))
        
        save_to_json(data)
        print(colored("\nData has been saved to ip_history.json", "green"))
    except requests.RequestException as e:
        print(colored(f"Error fetching IP information: {str(e)}", "red"))
    except json.JSONDecodeError:
        print(colored("Error parsing server response", "red"))
    except Exception as e:
        print(colored(f"An unexpected error occurred: {str(e)}", "red"))

def password_generator():
    random_color = random.choice(["red", "green", "yellow", "blue", "magenta", "cyan", "white"])
    
    title = pyfiglet.figlet_format("PASSWORD GENERATOR")
    colored_title = colored(title, random_color)
    print(colored_title)
    
    # Passwortlänge vom Benutzer anfordern
    try:
        length = int(input(colored("Enter the password length: ", "yellow")))
    except ValueError:
        print(colored("Invalid input. Please enter a number.", "red"))
        return
    
    if length < 6:
        print(colored("Password length should be at least 6 characters for security reasons.", "red"))
        return

    # Zeichenpool: Großbuchstaben, Kleinbuchstaben, Ziffern und Sonderzeichen
    chars = string.ascii_letters + string.digits + string.punctuation
    
    # Passwort generieren
    password = ''.join(random.choice(chars) for _ in range(length))
    
    # Farbig ausgeben
    print(colored(f"\nGenerated Password: {password}\n", random_color))

def my_ip():
    ip_title = pyfiglet.figlet_format("MY IP")
    random_color = random.choice(["red", "green", "yellow", "blue", "magenta", "cyan", "white"])
    colored_ip_title = colored(ip_title, random_color)
    print(colored_ip_title)
    try:
        response = requests.get('https://api.ipify.org?format=json')
        ip_data = response.json()
        print(colored(f"\nYour IP address is: {ip_data['ip']}\n", 'green'))
    except Exception as e:
        print(colored(f"\nError getting IP address: {str(e)}\n", 'red'))

def webscrape():
    webscrape_title = pyfiglet.figlet_format("WEBSCRAPER")
    random_color = random.choice(["red", "green", "yellow", "blue", "magenta", "cyan", "white"])
    colored_webscrape_title = colored(webscrape_title, random_color)
    print(colored_webscrape_title)

    url = input(colored("Enter the URL: ", "yellow")).strip()
    
    # Validate URL
    try:
        result = urlparse(url)
        if not all([result.scheme, result.netloc]):
            print(colored("Invalid URL. Please include http:// or https://", "red"))
            return
    except Exception:
        print(colored("Invalid URL format", "red"))
        return

    try:
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'}
        response = requests.get(url, headers=headers, timeout=10)
        response.raise_for_status()
        
        # Parse with BeautifulSoup
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Extract useful information
        print(colored("\nWebpage Analysis:", "green"))
        print(colored(f"Title: {soup.title.string if soup.title else 'No title found'}", random_color))
        
        # Extract all links
        print(colored("\nLinks found:", "green"))
        for link in soup.find_all('a', href=True):
            href = link['href']
            if href.startswith('http'):
                print(colored(f"- {href}", random_color))
        
        # Extract headings
        print(colored("\nHeadings:", "green"))
        for heading in soup.find_all(['h1', 'h2', 'h3']):
            print(colored(f"- {heading.get_text().strip()}", random_color))
        
        # Option to save content
        save = input(colored("\nDo you want to save the page content? (y/n): ", "yellow")).lower()
        if save == 'y':
            filename = f"webpage_{datetime.now().strftime('%Y%m%d_%H%M%S')}.html"
            with open(filename, 'w', encoding='utf-8') as f:
                f.write(response.text)
            print(colored(f"\nContent saved to {filename}", "green"))
            
    except requests.RequestException as e:
        print(colored(f"Error fetching webpage: {str(e)}", "red"))
    except Exception as e:
        print(colored(f"An unexpected error occurred: {str(e)}", "red"))

while True:
    multitool = pyfiglet.figlet_format("MULTI-TOOL", font="slant")
    random_color = random.choice(["red", "green", "yellow", "blue", "magenta", "cyan", "white"])
    colored_multitool = colored(multitool, random_color)
    print(colored_multitool)

    print(colored("[1] IP-TRACER", "blue"))
    print(colored("[2] PASSWORD GENERATOR", "blue"))
    print(colored("[3] WHAT IS MY IP?", "blue"))
    print(colored("[4] WEBSCRAPER", "blue"))
    print(colored("[5] EXIT", "red"))

    choice = input(colored("Enter your choice: ", "yellow"))

    if choice == "1":
        ip_tracer()
    elif choice == "2":
        password_generator()
    elif choice == "3":
        my_ip()
    elif choice == "4":
        webscrape()
    elif choice == "5":
        print(colored("\nGoodbye!", "green"))
        break
    else:
        print(colored("\nInvalid choice. Please try again.", "red"))
    
    input(colored("\nPress Enter to continue...", "cyan"))
