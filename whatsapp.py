import pyautogui
import time
import random

contact_name = "Name of friend"
message = "This message is sent by .."

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
