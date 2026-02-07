import random
import tkinter as tk
from tkinter import messagebox


# Function to copy password to clipboard when clicked
def copy_to_clipboard(event):
    password = event.widget.cget("text")
    root.clipboard_clear()  # Clear clipboard
    root.clipboard_append(password)  # Append password to clipboard
    messagebox.showinfo("Copied", "Password copied to clipboard!")  # Show message


# Function to generate passwords
def generate_passwords():
    try:
        pwd_count = int(entry_pwd_count.get())  # Get number of passwords
        pwd_chars = int(entry_pwd_chars.get())  # Get number of characters
        if pwd_count <= 0 or pwd_chars <= 0:
            messagebox.showerror("Invalid Input", "Please enter positive numbers.")
            return
    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter valid numbers.")
        return

    password_characters = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789!@#$%&*^()_+-=[]{}|"
    passwords = []

    # Generate random passwords
    for _ in range(pwd_count):
        pwd = "".join(random.choice(password_characters) for _ in range(pwd_chars))
        passwords.append(pwd)

    # Clear previous results
    result_frame.pack_forget()
    result_frame.pack(pady=10)

    # Insert new passwords and allow clicking on the text for copying
    for widget in result_frame.winfo_children():
        widget.destroy()

    for i, pwd in enumerate(passwords, start=1):
        password_label = tk.Label(
            result_frame, text=pwd, bg="lightyellow", fg="black", font=("Arial", 12)
        )
        password_label.pack(pady=5)
        password_label.bind(
            "<Button-1>", copy_to_clipboard
        )  # Bind the click event to the label


# Create the main window
root = tk.Tk()
root.title("Random Password Generator")
root.geometry("500x600")
root.config(bg="lightblue")

# Labels and entry fields
label_pwd_count = tk.Label(root, text="Number of passwords:", bg="lightyellow")
label_pwd_count.pack(pady=10)
entry_pwd_count = tk.Entry(root)
entry_pwd_count.pack(pady=5)

label_pwd_chars = tk.Label(root, text="Number of characters:", bg="lightyellow")
label_pwd_chars.pack(pady=5)
entry_pwd_chars = tk.Entry(root)
entry_pwd_chars.pack(pady=5)

# Generate Button
generate_button = tk.Button(
    root, text="Generate Passwords", command=generate_passwords, bg="lightgreen"
)
generate_button.pack(pady=10)

# Frame to display generated passwords
result_frame = tk.Frame(root, bg="lightyellow")
result_frame.pack(pady=10)

# Start the Tkinter event loop
root.mainloop()
