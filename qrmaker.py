"""
QR Maker: A simple tool to create QR codes.
by MaTiN
"""

import os
from tkinter import Tk, Canvas, Entry, Label, Button, PhotoImage
from PIL import ImageTk, Image
import qrcode

def create_qr_code(text, qr_path):
    """
    Create a QR code based on the given text and save it to the specified path.
    """
    qr = qrcode.make(text)
    qr.save(qr_path)

def display_qr_code(qr_path):
    """
    Display the QR code image on the canvas.
    """
    if os.path.exists(qr_path):
        img = Image.open(qr_path)
        img = img.resize((300, 300), Image.LANCZOS)
        photo = ImageTk.PhotoImage(img)
        label = Label(root, image=photo, width=300, height=300)
        label.image = photo
        canvas.create_window(200, 300, window=label)
    else:
        # Check again after 100 milliseconds
        root.after(100, lambda: display_qr_code(qr_path))

def create_qr_button_clicked():
    """
    Handle the button click event for creating QR codes.
    """
    text = entry.get()
    qr_path = "C:/Users/MaTiN/Desktop/myScripts/qrmaker/qr.png"
    create_qr_code(text, qr_path)
    display_qr_code(qr_path)

# Create the main Tkinter window
root = Tk()
root.title("QR Maker")

# Load the icon photo
ICON_PATH = "C:/Users/MaTiN/Desktop/myScripts/qrmaker/icon.png"
icon_photo = PhotoImage(file=ICON_PATH)
root.iconphoto(False, icon_photo)

# Set up the canvas
canvas = Canvas(root, width=400, height=510, bg="#3d3d3b")
canvas.pack()

# Entry widget for user input
entry = Entry(root, width=30)
entry_window = canvas.create_window(200, 50, window=entry)

# Button to trigger QR code creation
create_qr_button = Button(root, text="Create", command=create_qr_button_clicked
, bg="white", fg="black")
canvas.create_window(200, 100, window=create_qr_button)

# Label for author information
author_label = Label(root, text="by MaTiN", fg="white", bg="#3d3d3b"
, font=('Helvetica', 10, 'bold'))
canvas.create_window(200, 500, window=author_label)

if __name__ == "__main__":
    root.mainloop()
