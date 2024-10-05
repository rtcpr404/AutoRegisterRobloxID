from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import random
import string
import time
from datetime import datetime
from selenium.webdriver.common.by import By

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

def create_browser():
    try:
        brave_path = "C:/Program Files/BraveSoftware/Brave-Browser/Application/brave.exe"  # ระบุพาธไปยัง Brave
        chrome_driver_path = "C:/Users/rtcpr/Downloads/aut0s1gnup/lib/chromedriver.exe"  # ระบุพาธไปยัง Chromedriver

        options = Options()
        options.binary_location = brave_path
        options.add_argument("--incognito")  # เปิดโหมด private
        service = Service(executable_path=chrome_driver_path)
        driver = webdriver.Chrome(service=service, options=options)
        return driver
    except Exception as e:
        print(f"Error creating browser: {e}")
        return None

def create_account(driver):
    try:
        driver.get("https://www.roblox.com/CreateAccount")
        
        random_month = random.choice(["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"])
        days_in_month = {
            "Jan": 31, "Feb": 28, "Mar": 31, "Apr": 30,
            "May": 31, "Jun": 30, "Jul": 31, "Aug": 31,
            "Sep": 30, "Oct": 31, "Nov": 30, "Dec": 31
        }
        random_year = random.randint(datetime.now().year - 50, datetime.now().year - 13)
        random_day = random.randint(1, days_in_month[random_month])

        time.sleep(random.uniform(0.1, 1))
        driver.find_element(By.ID, "MonthDropdown").send_keys(random_month)
        time.sleep(random.uniform(0.1, 1))
        driver.find_element(By.ID, "DayDropdown").send_keys(f"{random_day:02d}")
        time.sleep(random.uniform(0.1, 1))
        driver.find_element(By.ID, "YearDropdown").send_keys(str(random_year))

        username = generate_username()
        time.sleep(random.uniform(0.1, 1))
        driver.find_element(By.ID, "signup-username").send_keys(username)

        password = generate_password()
        time.sleep(random.uniform(0.1, 1))
        driver.find_element(By.ID, "signup-password").send_keys(password)

        time.sleep(random.uniform(0.1, 1))
        driver.find_element(By.ID, "signup-button").click()

        time.sleep(5)  # รอให้หน้าเปลี่ยนไปหน้า home

        roblosecurity_cookie = None
        for cookie in driver.get_cookies():
            if cookie['name'] == '.ROBLOSECURITY':
                roblosecurity_cookie = cookie['value']
                break

        if roblosecurity_cookie:
            with open("cookies.txt", "a") as cookie_file:
                cookie_file.write(roblosecurity_cookie + "\n")

        return username, password

    except Exception as e:
        print(f"An error occurred during account creation: {e}")
        return None, None

accounts = []

execution_count = input("\nHow many accounts do you want to create?\nDefault value (1)\nAmount: ")
if not execution_count:
    execution_count = 1
else:
    try:
        execution_count = int(execution_count)
    except ValueError:
        print("Invalid number.")
        execution_count = 1

for _ in range(execution_count):
    driver = create_browser()
    if not driver:
        break
    username, password = create_account(driver)
    if username and password:
        accounts.append({"username": username, "password": password})
    driver.quit()

with open("accounts.txt", "a") as f:
    for account in accounts:
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        f.write(f"Username: {account['username']}, Password: {account['password']} (Created at {timestamp})\n")

print("\nAll accounts have been created. Accounts' details:\n")
for account in accounts:
    print(f"Username: {account['username']}, Password: {account['password']}")
print("\nSaved to the file accounts.txt and Cookies file Cookies.txt.")
