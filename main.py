import random
import string
import time
from datetime import datetime
from DrissionPage import ChromiumPage
from lib.lib import Main

lib = Main()

print("\nEnsuring Chrome availability...")

def generate_password():
    length = random.randint(8, 10)
    special_characters = string.punctuation.replace('(', '').replace(')', '').replace('{', '').replace('}', '').replace('[', '').replace(']', '')
    all_characters = string.ascii_lowercase + string.ascii_uppercase + string.digits + special_characters
    
    password = [
        random.choice(string.ascii_uppercase),
        random.choice(string.digits),
        random.choice(special_characters)
    ]
    
    special_char_count = random.randint(1, 2)
    password += random.choices(special_characters, k=special_char_count)
    password += random.choices(all_characters, k=length - len(password))
    random.shuffle(password)
    return ''.join(password)

def generate_username():
    length = random.randint(8, 12)
    characters = string.ascii_letters + string.digits
    username = ''.join(random.choices(characters, k=length))
    return username

accounts = []

while True:
    executionCount = input("\nHow many accounts do you want to create?\nDefault value (1)\nAmount: ")
    if executionCount == "":
        executionCount = 1
        break
    else:
        try:
            executionCount = int(executionCount)
            break
        except ValueError:
            print("Invalid number.")

def create_browser():
    try:
        page = ChromiumPage()
        return page
    except Exception as e:
        print(f"Error creating browser: {e}")
        return None

for x in range(int(executionCount)):
    page = create_browser()
    if not page:
        break
    try:
        page.get("https://www.roblox.com/CreateAccount")
        
        random_month = random.choice(["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"])
        random_day = random.randint(1, 28)
        random_year = random.randint(datetime.now().year - 50, datetime.now().year - 13)

        time.sleep(random.uniform(0.7, 1))
        page.ele("#MonthDropdown").select.by_value(random_month)
        time.sleep(random.uniform(0.1, 1))
        page.ele("#DayDropdown").select.by_value(f"{random_day:02d}")
        time.sleep(random.uniform(0.1, 1))
        page.ele("#YearDropdown").select.by_value(str(random_year))

        username = generate_username()
        time.sleep(random.uniform(0.1, 1))
        page.ele("#signup-username").input(username)

        password = generate_password()
        time.sleep(random.uniform(0.1, 1))
        page.ele("#signup-password").input(password)

        time.sleep(random.uniform(0.7, 1))
        page.ele("#signup-button").click()

    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        page.wait.url_change("https://www.roblox.com/home", timeout=float('inf'))
        
        roblosecurity_cookie = None
        for cookie in page.get_cookies():
            if cookie['name'] == '.ROBLOSECURITY':
                roblosecurity_cookie = cookie['value']
                break

        if roblosecurity_cookie:
            with open("cookies.txt", "a") as cookie_file:
                cookie_file.write(roblosecurity_cookie + "\n")

        accounts.append({"username": username, "password": password})
        page.quit()

with open("accounts.txt", "a") as f:
    for account in accounts:
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        f.write(f"Username: {account['username']}, Password: {account['password']} (Created at {timestamp})\n")

print("\nAll accounts have been created. Accounts' details:\n")
for account in accounts:
    print(f"Username: {account['username']}, Password: {account['password']}")
print("\nSaved to the file accounts.txt and Cookies file Cookies.txt.")
