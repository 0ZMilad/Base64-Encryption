import tkinter as tk
import pybase64
from tkinter import messagebox, filedialog

# Create the main application window
root = tk.Tk()
root.title('Encryption Base64')
FONT_STYLE = ("Fira Code", 18)
root.geometry("500x400")

root.configure(bg="dark grey")

# Function to insert a file and encode its content
def insert_file():
    file_path = filedialog.askopenfilename()
    if file_path:
        with open(file_path, 'rb') as file:
            file_content = file.read()
            encoded_content = pybase64.b64encode(file_content).decode("ascii")
            my_text.delete(1.0, tk.END)
            my_text.insert(tk.END, encoded_content)

# Function to clear the text box
def clear():
    my_text.delete(1.0, tk.END)
    my_entry.delete(0, tk.END)

# Function to encrypt the content
def encrypt():
    secret = my_text.get(1.0, tk.END)
    my_text.delete(1.0, tk.END)
    if my_entry.get() == "elder":
        secret = secret.encode("ascii")
        secret = pybase64.b64encode(secret)
        secret = secret.decode("ascii")
        my_text.insert(tk.END, secret)
    else:
        messagebox.showwarning("Incorrect!", "Incorrect Password, Try Again!")

# Function to decrypt the content
def decrypt():
    secret = my_text.get(1.0, tk.END)
    my_text.delete(1.0, tk.END)
    if my_entry.get() == "elder":
        secret = secret.encode("ascii")
        secret = pybase64.b64decode(secret)
        secret = secret.decode("ascii")
        my_text.insert(tk.END, secret)
    else:
        messagebox.showwarning("Incorrect!", "Incorrect Password, Try Again!")

# Create a frame for buttons
my_frame = tk.Frame(root)
my_frame.pack(pady=20)

# Create buttons for various actions
enc_button = tk.Button(my_frame, text="Encrypt", command=encrypt)
enc_button.grid(row=0, column=0)

dec_button = tk.Button(my_frame, text="Decrypt", command=decrypt)
dec_button.grid(row=0, column=1, padx=20)

clear_button = tk.Button(my_frame, text="Clear", command=clear)
clear_button.grid(row=0, column=2)

insert_button = tk.Button(my_frame, text="Insert Text-File", command=insert_file)
insert_button.grid(row=0, column=3, padx=5)

# Create labels, text boxes, and entry fields
enc_label = tk.Label(root, text="Encrypt/Decrypt Text." )
enc_label.pack()

my_text = tk.Text(root, width=57, height=10)
my_text.pack(pady=10)

password_label = tk.Label(root, text="Enter Your Password.")
password_label.pack()

my_entry = tk.Entry(root, font=("Helvetica", 18), width=35, show="*")
my_entry.pack(pady=10)

# Start the main event loop
root.mainloop()
