from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
import random

# Replace these with your target contact's name and the message to be sent
contact_name = "𝑴𝒂𝒚𝒂𝒏𝒌"
message = "This message is sent by AI"

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

