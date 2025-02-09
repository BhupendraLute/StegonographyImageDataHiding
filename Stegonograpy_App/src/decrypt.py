import cv2
from tkinter import messagebox

def decode_message(image_path, passcode):
    if not image_path:
        messagebox.showerror("Error", "Please select an image.")
        return None

    img = cv2.imread(image_path)
    if img is None:
        messagebox.showerror("Error", "Image not found!")
        return None

    binary_message = ""
    for row in img:
        for pixel in row:
            for channel in pixel:
                binary_message += str(channel & 1)

    chars = [binary_message[i:i+8] for i in range(0, len(binary_message), 8)]
    decrypted_text = ''.join(chr(int(char, 2)) for char in chars).split("\x00")[0]

    # Decrypt with passcode (simple XOR)
    try:
        original_message = ''.join(chr(ord(c) ^ ord(passcode[i % len(passcode)])) for i, c in enumerate(decrypted_text))
    except Exception:
        messagebox.showerror("Error", "Decryption failed. Ensure correct passcode.")
        return None

    if not original_message:
        messagebox.showerror("Error", "Incorrect passcode or no hidden message found.")
        return None
    
    return original_message
