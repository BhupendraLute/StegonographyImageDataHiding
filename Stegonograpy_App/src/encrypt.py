import cv2
import numpy as np
from tkinter import messagebox

def encode_message(image_path, message, passcode, output_path="encoded_image.png"):
    if not image_path:
        messagebox.showerror("Error", "Please select an image.")
        return
    
    img = cv2.imread(image_path)
    if img is None:
        messagebox.showerror("Error", "Image not found!")
        return

    # Encrypt message with passcode (simple XOR)
    encrypted_message = ''.join(chr(ord(c) ^ ord(passcode[i % len(passcode)])) for i, c in enumerate(message))
    binary_message = ''.join(format(ord(char), '08b') for char in encrypted_message) + '00000000'  # Null terminator

    rows, cols, channels = img.shape
    binary_index = 0

    if len(binary_message) > rows * cols * 3:
        messagebox.showerror("Error", "Message is too long for this image.")
        return

    for row in range(rows):
        for col in range(cols):
            for channel in range(3):  # Iterate through RGB
                if binary_index < len(binary_message):
                    img[row, col, channel] = (img[row, col, channel] & 0xFE) | int(binary_message[binary_index])
                    binary_index += 1
                else:
                    cv2.imwrite(output_path, img)
                    messagebox.showinfo("Success", f"Message encrypted and saved as {output_path}")
                    return
