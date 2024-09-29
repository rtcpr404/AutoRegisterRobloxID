# Let's create the README file with the provided content

readme_content = """
# Roblox Account Generator

This script automates the creation of Roblox accounts using a headless browser with the `DrissionPage` library. It randomly generates usernames, strong passwords, and handles the sign-up process on the Roblox website. The `.ROBLOSECURITY` cookie and account credentials are stored for later use.

## 🚀 Features

- **Random Username & Password Generation**: Creates secure account credentials with a mix of letters, digits, and special characters.
- **Automated Sign-Up Process**: Fills in the registration form on the Roblox website, including randomized birth dates.
- **Cookie Storage**: Saves the `.ROBLOSECURITY` cookie in `cookies.txt` for each created account.
- **Account Storage**: Stores the account details (username, password) in `accounts.txt` with timestamps.

## 🛠️ Requirements

- **Python 3.x**
- **DrissionPage** library
- **Chromium** (for headless browser automation)

### Install Dependencies

1. Install the required Python packages:

    ```bash
    pip install DrissionPage
    ```

2. Ensure Chromium is installed and accessible by the script.

## 📝 Usage

1. **Run the script:**

    ```bash
    python main.py
    ```

2. **Enter the number of accounts** you want to create when prompted. Press Enter to default to 1 account.

3. The script will generate and store the account information in the following files:
   - `accounts.txt` — Stores the usernames and passwords.
   - `cookies.txt` — Stores the `.ROBLOSECURITY` cookies.

### Example Output

- **accounts.txt:**

    ```txt
    Username: user123456, Password: Passw0rd! (Created at 2024-09-29 17:00:00)
    ```

- **cookies.txt:**

    ```txt
    .ROBLOSECURITY_COOKIE_VALUE_1
    ```

## ⚙️ Customization

You can modify the following functions to adjust the behavior of username and password generation:

- `generate_username()`: Modify how usernames are generated, including length and character set.
- `generate_password()`: Customize password length and complexity.

## 🛡️ Notes

- Ensure your internet connection is stable while running the script.
- The script includes random delays between actions to mimic human behavior and reduce the risk of bot detection.

## 📂 File Structure

```bash
.
├── main.py    # Main script file
├── accounts.txt            # File to store created account details
├── cookies.txt             # File to store ROBLOSECURITY cookies
└── lib/
    └── lib.py              # Contains the 'Main' class used by the script
