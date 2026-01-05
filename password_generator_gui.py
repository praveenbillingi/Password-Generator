import tkinter as tk
from tkinter import messagebox
import random
import string

# Function to check password strength
def check_strength(password):
    has_letter = any(c.isalpha() for c in password)
    has_digit = any(c.isdigit() for c in password)
    has_symbol = any(c in string.punctuation for c in password)

    if len(password) < 6:
        return "Weak", "red"
    elif has_letter and has_digit and not has_symbol:
        return "Medium", "orange"
    elif has_letter and has_digit and has_symbol:
        return "Strong", "green"
    else:
        return "Weak", "red"

# Generate password
def generate_password():
    try:
        length = int(length_entry.get())
        if length <= 0:
            messagebox.showerror("Error", "Enter a positive number")
            return

        characters = string.ascii_letters + string.digits + string.punctuation
        password = "".join(random.choice(characters) for _ in range(length))

        password_entry.delete(0, tk.END)
        password_entry.insert(0, password)

        strength, color = check_strength(password)
        strength_label.config(text=f"Strength: {strength}", fg=color)

    except ValueError:
        messagebox.showerror("Error", "Please enter a valid number")

# Copy password
def copy_password():
    root.clipboard_clear()
    root.clipboard_append(password_entry.get())
    messagebox.showinfo("Copied", "Password copied to clipboard")

# GUI setup
root = tk.Tk()
root.title("Password Generator")
root.geometry("420x300")
root.resizable(False, False)

tk.Label(root, text="Password Generator", font=("Arial", 16, "bold")).pack(pady=10)

tk.Label(root, text="Enter Password Length:").pack()
length_entry = tk.Entry(root, width=20)
length_entry.pack(pady=5)

tk.Button(root, text="Generate Password", command=generate_password).pack(pady=10)

password_entry = tk.Entry(root, width=38)
password_entry.pack(pady=5)

strength_label = tk.Label(root, text="Strength: ", font=("Arial", 11, "bold"))
strength_label.pack(pady=5)

tk.Button(root, text="Copy Password", command=copy_password).pack(pady=10)

root.mainloop()