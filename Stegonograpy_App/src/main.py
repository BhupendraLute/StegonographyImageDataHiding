import tkinter as tk
from tkinter import filedialog, messagebox, scrolledtext
from tkinter import ttk
import threading
from encrypt import encode_message
from decrypt import decode_message
from utils import select_image, style_label, style_entry, style_button

# GUI Setup
root = tk.Tk()
root.title("Secure Image Steganography")
root.geometry("600x520")
root.configure(bg="#e0e0e0")

# Tabbed Interface
notebook = ttk.Notebook(root, padding=5)
encrypt_frame = tk.Frame(notebook, padx=10, pady=10, bg="#f9f9f9")
decrypt_frame = tk.Frame(notebook, padx=10, pady=10, bg="#f9f9f9")
about_frame = tk.Frame(notebook, padx=10, pady=10, bg="#f9f9f9")  
notebook.add(encrypt_frame, text="Encrypt")
notebook.add(decrypt_frame, text="Decrypt")
notebook.add(about_frame, text="About")
notebook.pack(expand=True, fill="both", pady=10)

# About Tab Content
tk.Label(about_frame, text="About This Application", font=("Arial", 14, "bold"), bg="#f9f9f9").pack(pady=10)
tk.Label(about_frame, text="Secure image steganography using LSB technique.", bg="#f9f9f9", wraplength=500).pack(pady=5)
tk.Label(about_frame, text="Developed by: Bhupendra Lute", bg="#f9f9f9", font=("Arial", 12)).pack(pady=5)
tk.Label(about_frame, text="Email: bhupendralute1234@gmail.com", bg="#f9f9f9", font=("Arial", 12)).pack(pady=5)
tk.Label(about_frame, text="Github: https://github.com/BhupendraLute/StegonographyImageDataHiding", bg="#f9f9f9", font=("Arial", 12)).pack(pady=5)

# Encryption UI
style_label(encrypt_frame, "Select Image:", 0)
encrypt_image_label = tk.Label(encrypt_frame, text="No file selected", wraplength=250, bg="#f9f9f9")
encrypt_image_label.grid(row=0, column=1)
tk.Button(encrypt_frame, text="Browse", command=lambda: select_image(encrypt_image_label)).grid(row=0, column=2)

style_label(encrypt_frame, "Enter Secret Message:", 1)
message_text = scrolledtext.ScrolledText(encrypt_frame, width=40, height=10, font=("Arial", 12), padx=5, pady=5)
message_text.grid(row=1, column=1, columnspan=2, pady=10)

style_label(encrypt_frame, "Enter Passcode:", 2)
passcode_entry = style_entry(encrypt_frame, 2, "*")

style_button(encrypt_frame, "Encrypt & Save", lambda: encode_message(encrypt_image_label.cget("text"), message_text.get("1.0", tk.END).strip(), passcode_entry.get()), 3)

# Decryption UI
style_label(decrypt_frame, "Select Encrypted Image:", 0)
decrypt_image_label = tk.Label(decrypt_frame, text="No file selected", wraplength=250, bg="#f9f9f9")
decrypt_image_label.grid(row=0, column=1)
tk.Button(decrypt_frame, text="Browse", command=lambda: select_image(decrypt_image_label)).grid(row=0, column=2)

tk.Label(decrypt_frame, text="Note: Larger Image size takes more time to decrypt", bg="#f9f9f9", font=("Arial", 12)).grid(row=1, column=0, columnspan=3, pady=5)

style_label(decrypt_frame, "Enter Passcode:", 2)
decrypt_passcode_entry = style_entry(decrypt_frame, 2, "*")

progress = ttk.Progressbar(decrypt_frame, mode="indeterminate")
decrypted_label = tk.Label(decrypt_frame, text="Decrypted Message:", bg="#f9f9f9", font=("Arial", 12))
decrypted_textbox = scrolledtext.ScrolledText(decrypt_frame, width=50, height=10, font=("Arial", 12), padx=5, pady=5)

def handle_decryption():
    def decrypt_process():
        progress.grid(row=3, column=0, columnspan=3, pady=10)
        progress.start()
        decrypted_textbox.delete("1.0", tk.END)
        decrypted_label.grid(row=4, column=0, columnspan=3, pady=5, sticky="w")
        decrypted_textbox.grid(row=5, column=0, columnspan=3, pady=5, sticky="w")
        root.update_idletasks()
        decrypted_text = decode_message(decrypt_image_label.cget("text"), decrypt_passcode_entry.get())
        progress.stop()
        progress.grid_forget()
        if decrypted_text:
            decrypted_textbox.insert(tk.END, decrypted_text)
        else:
            decrypted_textbox.insert(tk.END, "Error: Incorrect passcode or no hidden message found.")
    
    threading.Thread(target=decrypt_process).start()

style_button(decrypt_frame, "Decrypt & Read", handle_decryption, 3)



root.mainloop()
