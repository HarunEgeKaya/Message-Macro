import pyautogui
import time
import tkinter as tk
import threading

message = "Your Tex"

def write_message():
    time.sleep(5)
    while True:
        pyautogui.typewrite(message + '\n', interval=0.0005)
        time.sleep(1)

def on_click():
    threading.Thread(target=write_message, daemon=True).start()

root = tk.Tk()
root.title("Message Macro")

send_button = tk.Button(root, text="Start", command=on_click)
send_button.pack(pady=20)

root.mainloop()
