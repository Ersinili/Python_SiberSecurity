import tkinter as tk
import subprocess

def run_impulse():
    target = target_entry.get()
    method = method_entry.get()
    time = time_entry.get()
    threads = threads_entry.get()

    command = ["python", "impulse.py", "--target", target, "--method", method, "--time", time, "--threads", threads]
    subprocess.Popen(command)

# Tkinter penceresini oluştur
window = tk.Tk()
window.title("Impulse Attack")
window.configure(bg="white")

# Bilgilendirme kutusu
info_label = tk.Label(window, text="""-h, --help Yardım mesajını göster ve çıkış yap
--target <IP:PORT, URL, PHONE> Hedef IP:port, URL veya telefon numarası
Saldırı yöntemi --method <SMS/EMAIL/NTP/UDP/SYN/ICMP/POD/SLOWLORIS/MEMCACHED/HTTP>
-time <zaman> Süre (saniye)
--threads <iş parçacığı> İş parçacığı sayısı (1-200)""", bg="white", fg="black")
info_label.pack(pady=10)

# Hedef IP:PORT etiketi ve giriş alanı
target_label = tk.Label(window, text="Hedef IP:PORT", bg="white", fg="black")
target_label.pack()

target_entry = tk.Entry(window)
target_entry.pack()

# Saldırı yöntemi etiketi ve giriş alanı
method_label = tk.Label(window, text="Saldırı Yöntemi", bg="white", fg="black")
method_label.pack()

method_entry = tk.Entry(window)
method_entry.pack()

# Süre etiketi ve giriş alanı
time_label = tk.Label(window, text="Süre (saniye)", bg="white", fg="black")
time_label.pack()

time_entry = tk.Entry(window)
time_entry.pack()

# İş parçacığı sayısı etiketi ve giriş alanı
threads_label = tk.Label(window, text="İş Parçacığı Sayısı", bg="white", fg="black")
threads_label.pack()

threads_entry = tk.Entry(window)
threads_entry.pack()

# Çalıştır düğmesi
run_button = tk.Button(window, text="Çalıştır", font=("Arial", 12), padx=10, pady=5, bg="white", fg="black", command=run_impulse)
run_button.pack(pady=10)

window.mainloop()
