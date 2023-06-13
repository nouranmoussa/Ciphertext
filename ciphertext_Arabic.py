""""F(p)= (p+k) mod m
    k -> key
    m -> number of alphabet of the used language"""

import tkinter as tk
import arabic_reshaper

def encrypt_arabic(text, key):
    result = ""
    for char in text:
        if char.isalpha():
            # Shift the character by the key value
            shifted = (ord(char) - 1568 + key) % 16384
            result += chr(shifted + 1568)
        else:
            # Leave non-alphabetic characters unchanged
            result += char
    return result

def decrypt_arabic(text, key):
    result = ""
    for char in text:
        if char.isalpha():
            # Shift the character back by the key value
            shifted = (ord(char) - 1568 - key) % 16384
            result += chr(shifted + 1568)
        else:
            # Leave non-alphabetic characters unchanged
            result += char
    return result

def encrypt():
    message = message_input.get("1.0", tk.END).strip()
    key = int(key_entry.get())
    encrypted_message = encrypt_arabic(message, key)
    result_input.delete("1.0", tk.END)
    result_input.insert(tk.END, encrypted_message)

def decrypt():
    message = message_input.get("1.0", tk.END).strip()
    key = int(key_entry.get())
    decrypted_message = decrypt_arabic(message, key)
    # Check if the message is encrypted before reshaping and reversing it
    if any(1568 <= ord(c) <= 16383 for c in decrypted_message):
        decrypted_message = arabic_reshaper.reshape(decrypted_message)
        decrypted_message = decrypted_message[::-1]
        result_input.delete("1.0", tk.END)
        result_input.insert(tk.END, decrypted_message)
    else:
        result_input.delete("1.0", tk.END)
        result_input.insert(tk.END, "Error: Message is not encrypted.")

# Create tkinter window
root = tk.Tk()
root.title("Arabic Text Encoder/Decoder")

# Create input widgets
message_label = tk.Label(root, text="Message:")
message_label.pack()
message_input = tk.Text(root, height=5)
message_input.pack()

# Create key input widget
key_label = tk.Label(root, text="Key:")
key_label.pack()
key_entry = tk.Entry(root)
key_entry.pack()

# Create encrypt and decrypt buttons
encrypt_button = tk.Button(root, text="Encrypt", command=encrypt)
encrypt_button.pack()
decrypt_button = tk.Button(root, text="Decrypt", command=decrypt)
decrypt_button.pack()

# Create output widget
result_label = tk.Label(root, text="Result:")
result_label.pack()
result_input = tk.Text(root, height=5)
result_input.pack()

root.mainloop()
