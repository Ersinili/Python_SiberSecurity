import tkinter as tk
import subprocess

def run_exploit():
    # Exploit projesinin çalıştırılması için gerekli kodlar
    command = ["python", "exploit.py"]
    subprocess.Popen(command)

def run_impulse():
    # Impulse projesinin çalıştırılması için gerekli kodlar
    command = ["python", "impulse_giris.py"]
    subprocess.Popen(command)

def run_keylogger():
    # Keylogger projesinin çalıştırılması için gerekli kodlar
    command = ["python", "Keylogger.py"]
    subprocess.Popen(command)

def submit_project():
    selected_project = project_var.get()
    if selected_project == "Exploit":
        run_exploit()
    elif selected_project == "Impulse":
        run_impulse()
    elif selected_project == "Keylogger":
        run_keylogger()

# Tkinter penceresini oluştur
window = tk.Tk()
window.title("Project Selector")
window.configure(bg="white")

# Proje seçeneklerini içeren bir liste
project_options = ["Exploit", "Impulse", "Keylogger"]

project_var = tk.StringVar()

option_frame = tk.Frame(window, bg="white")
option_frame.pack(pady=10)

button_font = ("Arial", 12)

for option in project_options:
    button = tk.Radiobutton(option_frame, text=option, variable=project_var, value=option,
                            font=button_font, padx=10, pady=5,
                            bg="white", fg="black")
    button.pack(side=tk.LEFT, padx=5)

submit_button = tk.Button(window, text="Submit", font=button_font, padx=10, pady=5,
                          bg="white", fg="black", command=submit_project)
submit_button.pack(pady=10)

window.mainloop()
