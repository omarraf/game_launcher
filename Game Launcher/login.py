import tkinter as tk
from tkinter import messagebox
import subprocess
import json
import os

# File to store user data
USER_FILE = "users.json"

# Load user data
def load_users():
    if os.path.exists(USER_FILE):
        with open(USER_FILE, "r") as file:
            return json.load(file)
    return {}

# Save user data
def save_users(users):
    with open(USER_FILE, "w") as file:
        json.dump(users, file)

# Validate login
def validate_login(username, password, root):
    users = load_users()
    if username in users and users[username] == password:
        messagebox.showinfo("Login Successful", "Welcome to Fullerton Funhouse!")
        root.destroy()  # Close the login window
        subprocess.Popen(["python", "game_launcher.py"])  # Launch game launcher
    else:
        messagebox.showerror("Login Failed", "Invalid username or password. Please try again.")

# Register new user
def register_user(username, password, root):
    users = load_users()
    if username in users:
        messagebox.showerror("Registration Failed", "Username already exists. Please choose another one.")
    else:
        users[username] = password
        save_users(users)
        messagebox.showinfo("Registration Successful", "User registered successfully!")
        root.destroy()  # Close the registration window
        create_login_page()  # Go back to login page

# Create registration page
def create_registration_page():
    root = tk.Tk()
    root.title("Register - Fullerton Funhouse")
    root.geometry("400x300")
    root.configure(bg="#1e1e2f")

    # Title label
    title_label = tk.Label(root, text="Register for Fullerton Funhouse", font=("Arial", 16, "bold"), bg="#1e1e2f", fg="white")
    title_label.pack(pady=20)

    # Username and password entries
    username_label = tk.Label(root, text="Username:", font=("Arial", 12), bg="#1e1e2f", fg="white")
    username_label.pack(pady=5)
    username_entry = tk.Entry(root, font=("Arial", 12))
    username_entry.pack(pady=5)

    password_label = tk.Label(root, text="Password:", font=("Arial", 12), bg="#1e1e2f", fg="white")
    password_label.pack(pady=5)
    password_entry = tk.Entry(root, font=("Arial", 12), show="*")
    password_entry.pack(pady=5)

    # Register button
    register_button = tk.Button(
        root,
        text="Register",
        font=("Arial", 14),
        command=lambda: register_user(username_entry.get(), password_entry.get(), root),
        bg="#404040",
        fg="white"
    )
    register_button.pack(pady=20)

    root.mainloop()

# Create login page
def create_login_page():
    root = tk.Tk()
    root.title("Login - Fullerton Funhouse")
    root.geometry("400x300")
    root.configure(bg="#1e1e2f")

    # Title label
    title_label = tk.Label(root, text="Fullerton Funhouse - Game Launcher", font=("Arial", 16, "bold"), bg="#1e1e2f", fg="white")
    title_label.pack(pady=20)

    # Username and password entries
    username_label = tk.Label(root, text="Username:", font=("Arial", 12), bg="#1e1e2f", fg="white")
    username_label.pack(pady=5)
    username_entry = tk.Entry(root, font=("Arial", 12))
    username_entry.pack(pady=5)

    password_label = tk.Label(root, text="Password:", font=("Arial", 12), bg="#1e1e2f", fg="white")
    password_label.pack(pady=5)
    password_entry = tk.Entry(root, font=("Arial", 12), show="*")
    password_entry.pack(pady=5)

    # Login button
    login_button = tk.Button(
        root,
        text="Login",
        font=("Arial", 14),
        command=lambda: validate_login(username_entry.get(), password_entry.get(), root),
        bg="#404040",
        fg="white"
    )
    login_button.pack(pady=10)

    # Register button
    register_button = tk.Button(
        root,
        text="Register",
        font=("Arial", 12),
        command=lambda: [root.destroy(), create_registration_page()],  # Open registration page
        bg="#5050f0",
        fg="white"
    )
    register_button.pack(pady=10)

    root.mainloop()

# Run the login page
if __name__ == "__main__":
    create_login_page()
