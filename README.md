# Roblox Account Creator

This program is an automated tool for creating Roblox accounts using Python, Selenium, and Tkinter. It includes a GUI for specifying account creation parameters, such as the number of accounts, username prefix, and username length. The program automatically fills out registration forms on Roblox, solves CAPTCHA (manual intervention may be required), and saves `.ROBLOSECURITY` cookies along with the generated usernames and passwords to files `cookies.txt` and `Account.txt`.

## Features
- Automatically creates Roblox accounts using Selenium WebDriver
- GUI built with Tkinter for setting account creation details
- Randomly assigns gender for each created account
- Saves `.ROBLOSECURITY` cookie and generated usernames and passwords in files

## Installation

1. **Install ChromeDriver**:
   Download [ChromeDriver](https://sites.google.com/chromium.org/driver/) and place `chromedriver.exe` in the `webdriver` folder within your project directory.

2. **Install Required Libraries**:
   Create a virtual environment if desired, then install the necessary libraries:
   ```bash
   pip install selenium tkinter
