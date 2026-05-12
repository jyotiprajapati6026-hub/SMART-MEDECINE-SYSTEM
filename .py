import tkinter as tk
from tkinter import messagebox
from datetime import datetime

# Dummy Login Credentials
USERNAME = "admin"
PASSWORD = "1234"

medicines = []

# ================= LOGIN FUNCTION =================
def login():
    username = entry_username.get()
    password = entry_password.get()

    if username in users and users[username] == password:
        messagebox.showinfo("Login Success", "Welcome!")
    else:
        messagebox.showerror("Error", "Invalid Username or Password")
        def reset_password():
    
# ================= DASHBOARD =================
def open_dashboard():
    global root
    root = tk.Tk()
    root.title("💊 Smart Medicine Tracker")
    root.geometry("520x550")
    root.config(bg="#1e1e2f")

    def add_medicine():
        name = name_entry.get()
        time = time_entry.get()

        if name == "" or time == "":
            messagebox.showwarning("Warning", "⚠ Fill all fields")
            return

        medicines.append((name, time))
        update_list()
        name_entry.delete(0, tk.END)
        time_entry.delete(0, tk.END)

    def update_list():
        listbox.delete(0, tk.END)
        for med in medicines:
            listbox.insert(tk.END, f"💊 {med[0]}  ⏰ {med[1]}")

    def check_reminder():
        current_time = datetime.now().strftime("%H:%M")
        for med in medicines:
            if med[1] == current_time:
                messagebox.showinfo("Reminder", f"💊 Time to take {med[0]}")
        root.after(60000, check_reminder)

    # Title
    tk.Label(root, text="💊 Smart Medicine Tracker",
             font=("Helvetica", 18, "bold"),
             bg="#1e1e2f", fg="#00ffcc").pack(pady=15)

    # Frame
    frame = tk.Frame(root, bg="#2c2c3e")
    frame.pack(pady=10, padx=20, fill="x")

    tk.Label(frame, text="Medicine Name", bg="#2c2c3e", fg="white").grid(row=0, column=0, pady=8, padx=10)
    name_entry = tk.Entry(frame, width=25)
    name_entry.grid(row=0, column=1, pady=8)

    tk.Label(frame, text="Time (HH:MM)", bg="#2c2c3e", fg="white").grid(row=1, column=0, pady=8, padx=10)
    time_entry = tk.Entry(frame, width=25)
    time_entry.grid(row=1, column=1, pady=8)

    tk.Button(root, text="➕ Add Medicine",
              command=add_medicine,
              bg="#00b894", fg="white",
              font=("Arial", 12, "bold")).pack(pady=15)

    listbox = tk.Listbox(root, width=45, height=12,
                         bg="#2c2c3e", fg="#00ffcc")
    listbox.pack(pady=10)

    tk.Label(root, text="Stay Healthy 💚",
             bg="#1e1e2f", fg="gray").pack(pady=10)

    check_reminder()
    root.mainloop()

# ================= LOGIN UI =================
login_window = tk.Tk()
login_window.title("Login Page 🔐")
login_window.geometry("350x300")
login_window.config(bg="#1e1e2f")

tk.Label(login_window, text="🔐 Login",
         font=("Helvetica", 18, "bold"),
         bg="#1e1e2f", fg="#00ffcc").pack(pady=20)

tk.Label(login_window, text="Username",
         bg="#1e1e2f", fg="white").pack()
username_entry = tk.Entry(login_window)
username_entry.pack(pady=5)

tk.Label(login_window, text="Password",
         bg="#1e1e2f", fg="white").pack()
password_entry = tk.Entry(login_window, show="*")
password_entry.pack(pady=5)

tk.Button(login_window, text="Login",
          command=login,
          bg="#00b894", fg="white",
          font=("Arial", 12, "bold")).pack(pady=20)

login_window.mainloop()