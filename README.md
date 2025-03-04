# WhatsApp Automation Script

This repository contains two Python scripts that automate the process of sending messages on WhatsApp. The first script (`whatsapp.py`) uses **pyautogui** to send messages on WhatsApp Desktop app, while the second script (`web.py`) uses **Selenium** to automate WhatsApp Web.

---

## Files

### 1. `whatsapp.py` - Automate WhatsApp Desktop

This script uses `pyautogui` to automate the WhatsApp Desktop application. It performs actions like searching for a contact and sending messages, but only works on the WhatsApp Desktop app.

#### Prerequisites

- Python 3.x
- `pyautogui` library

You can install `pyautogui` using:
```bash
pip install pyautogui
```
## How it Works
- The script opens the WhatsApp Desktop application and waits for 5 seconds to ensure that the contact is selected.
- It searches for a contact by name using the search feature (Ctrl+F).
- The script continuously sends the predefined message ("This message is sent by AI") to the contact with random intervals.
Example Code:
```python
# copy
import pyautogui
import time
import random

contact_name = "Your Contact Name"
message = "Your Custom Message"

def send_whatsapp_message():
    print("Please make sure the chat with the contact is active!")
    time.sleep(5)

    pyautogui.hotkey('ctrl', 'f')
    time.sleep(1)
    pyautogui.write(contact_name)
    time.sleep(1)
    pyautogui.press('enter')

    while True:
        pyautogui.write(message)
        pyautogui.press('enter')
        print(f"Message sent: {message}")
        sleep_time = random.uniform(0, 1)
        time.sleep(sleep_time)

send_whatsapp_message()
```
### web.py - Automate WhatsApp Web with Selenium
- This script uses Selenium WebDriver to automate WhatsApp Web in a browser like Chrome. The script can open WhatsApp Web, log in (by scanning the QR code), search for a contact, and send messages.

Prerequisites
Python 3.x
selenium library
ChromeDriver (or the appropriate WebDriver for your browser)
You can install selenium using:

``` bash
# copy
pip install selenium
```
- You also need to install ChromeDriver (or your respective browser's WebDriver):

#### Download the latest ChromeDriver: ChromeDriver
- Ensure that the WebDriver version matches your browser version.
## How it Works
The script opens WhatsApp Web in a browser (e.g., Chrome).
It waits for you to scan the QR code for authentication.
Once logged in, it searches for the specified contact (Your Contact Name).
It sends the predefined message ("Your Custom Message") to the contact.
It repeats the process with random delays between messages.
Example Code:
``` python
# copy
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
import random

# Replace these with your target contact's name and the message to be sent
contact_name = "Your Contact Name"
message = "Your Custom Message"

# Path to your WebDriver (e.g., ChromeDriver)
driver_path = "/path/to/chromedriver"  # Replace with the path to your driver
driver = webdriver.Chrome(executable_path=driver_path)

def send_whatsapp_message():
    # Open WhatsApp Web
    driver.get("https://web.whatsapp.com/")
    print("Please scan the QR code on WhatsApp Web.")
    time.sleep(15)  # Wait for the user to scan the QR code (adjust if necessary)

    # Find the search box and type the contact's name
    search_box = driver.find_element(By.XPATH, '//*[@title="Search or start new chat"]')
    search_box.click()
    search_box.send_keys(contact_name)
    time.sleep(2)  # Wait for results to appear
    search_box.send_keys(Keys.ENTER)

    # Find the message input box and send the message in a loop
    while True:
        message_box = driver.find_element(By.XPATH, '//div[@contenteditable="true"][@data-tab="1"]')
        message_box.send_keys(message)
        message_box.send_keys(Keys.ENTER)
        print(f"Message sent: {message}")
        
        # Random sleep to mimic human behavior
        sleep_time = random.uniform(0.5, 2)
        time.sleep(sleep_time)

# Call the function to send messages
send_whatsapp_message()
```
## How to Use
- whatsapp.py (WhatsApp Desktop Automation)
- Install Python if not already installed (3.x).
-Install the required library pyautogui:
``` bash
# copy
pip install pyautogui
```
> Open WhatsApp Desktop on your system.
> Run the script:
``` bash
# copy
python whatsapp.py
```
- The script will wait for 5 seconds, then start sending the message to the specified contact on WhatsApp Desktop.
- web.py (WhatsApp Web Automation)
- Install Python if not already installed (3.x).
- Install the required library selenium:
```bash
# copy
pip install selenium
```
- Download the appropriate WebDriver for your browser (e.g., ChromeDriver for Chrome) and place it in a folder on your machine. You can download ChromeDriver here: ChromeDriver.
- Open WhatsApp Web on your browser and scan the QR code using your phone.
#### Run the script:
```bash
# copy
python web.py
``` 
### The script will wait for you to scan the QR code, then it will start searching for the contact and send the predefined message.
## Notes
> Browser Requirements: Make sure you have the correct version of chromedriver or geckodriver that matches your installed browser version.
>  WhatsApp Web: The script assumes you are already logged into WhatsApp Web and that your browser is able to load it correctly.
> Infinite Loop: Both scripts send messages in an infinite loop. Press Ctrl+C in the terminal to stop the script.
> Random Delays: The script includes random delays between messages to mimic human behavior and avoid detection as a bot.
## Conclusion
This repository provides two different approaches to automate WhatsApp messaging, one using pyautogui for the desktop app and another using Selenium for WhatsApp Web. You can choose whichever suits your needs best.

> Feel free to # copy-paste this markdown text directly into your `README.md` file!
