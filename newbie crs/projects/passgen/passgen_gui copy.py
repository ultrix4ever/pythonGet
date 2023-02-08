import tkinter as tk
import random
import string

def generate_password():
    password = "".join(random.choices(string.ascii_letters + string.digits, k=16))
    password_entry.delete(0, tk.END)
    password_entry.insert(0, password)

root = tk.Tk()
root.title("Password Generator")

password_label = tk.Label(root, text="Password:")
password_entry = tk.Entry(root, show="*", width=30)
generate_button = tk.Button(root, text="Generate", command=generate_password)

password_label.pack()
password_entry.pack()
generate_button.pack()

root.mainloop()