import tkinter as tk
from tkinter import filedialog

def select_image(label):
    file_path = filedialog.askopenfilename(filetypes=[("Image Files", "*.png;*.jpg;*.jpeg")])
    if file_path:
        label.config(text=file_path)
    return file_path

def style_label(frame, text, row):
    label = tk.Label(frame, text=text, bg="#f9f9f9", font=("Arial", 12))
    label.grid(row=row, column=0, pady=10, sticky="w")
    return label

def style_entry(frame, row, show_text=""):
    entry = tk.Entry(frame, width=40, font=("Arial", 12), show=show_text)
    entry.grid(row=row, column=1, columnspan=2, pady=10)
    return entry

def style_button(frame, text, command, row):
    button = tk.Button(frame, text=text, font=("Arial", 12, "bold"), bg="#4CAF50", fg="white", padx=10, pady=5, command=command)
    button.grid(row=row, column=0, columnspan=3, pady=15)
    return button
