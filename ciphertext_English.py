""""F(p)= (p+k) mod m
    k -> key
    m -> number of alphabet of the used language"""
import tkinter as tk

def encrypt(text, key):
    result = ""                               #Initialize an empty string to store the encrypted text
    for char in text:                         #Loop through each character in the input 
        if char.isalpha():                    #Check if the current character is a letter
            if char.isupper():                #Check if the current character is an uppercase letter
                # Shift the character by the key value
                shifted = (ord(char) - ord('A') + key) % 26
                result += chr(shifted + ord('A'))
            else:                             #Lower case
                # Shift the character by the key value
                shifted = (ord(char) - ord('a') + key) % 26
                result += chr(shifted + ord('a'))
        else:
            # Leave non-alphabetic characters unchanged
            result += char
    return result

def decrypt(text, key):
    result = ""
    for char in text:
        if char.isalpha():
            if char.isupper():
                # Shift the uppercase character back by the key value
                shifted = (ord(char) - ord('A') - key) % 26
                result += chr(shifted + ord('A'))
            else:
                # Shift the lowercase character back by the key value
                shifted = (ord(char) - ord('a') - key) % 26
                result += chr(shifted + ord('a'))
        else:
            # Leave non-alphabetic characters unchanged
            result += char
    return result

def encrypt_text():
    text = input_text.get("1.0", tk.END).strip()
    key = int(key_entry.get())
    encrypted_text = encrypt(text, key)
    output_text.delete("1.0", tk.END)
    output_text.insert(tk.END, encrypted_text)

def decrypt_text():
    text = input_text.get("1.0", tk.END).strip()
    key = int(key_entry.get())
    decrypted_text = decrypt(text, key)
    output_text.delete("1.0", tk.END)
    output_text.insert(tk.END, decrypted_text)

# Create tkinter window
root = tk.Tk()
root.title("English Text Encoder/Decoder")

# Create input widgets
input_label = tk.Label(root, text="Input Text:")
input_label.pack()
input_text = tk.Text(root, height=5)
input_text.pack()

# Create key input widget
key_label = tk.Label(root, text="Key:")
key_label.pack()
key_entry = tk.Entry(root)
key_entry.pack()

# Create encrypt and decrypt buttons
encrypt_button = tk.Button(root, text="Encrypt", command=encrypt_text)
encrypt_button.pack()
decrypt_button = tk.Button(root, text="Decrypt", command=decrypt_text)
decrypt_button.pack()

# Create output widget
output_label = tk.Label(root, text="Output Text:")
output_label.pack()
output_text = tk.Text(root, height=5)
output_text.pack()

root.mainloop()