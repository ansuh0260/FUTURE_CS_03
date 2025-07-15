from Crypto.Cipher import AES
import os

def pad(data):
    # Pads the data to be a multiple of 16 bytes (AES block size)
    return data + b' ' * (16 - len(data) % 16)

def encrypt_file(input_path, output_path, key):
    with open(input_path, 'rb') as f:
        data = f.read()
    cipher = AES.new(key, AES.MODE_ECB)
    encrypted_data = cipher.encrypt(pad(data))
    with open(output_path, 'wb') as f:
        f.write(encrypted_data)

def decrypt_file(input_path, output_path, key):
    with open(input_path, 'rb') as f:
        encrypted_data = f.read()
    cipher = AES.new(key, AES.MODE_ECB)
    decrypted_data = cipher.decrypt(encrypted_data).rstrip(b' ')
    with open(output_path, 'wb') as f:
        f.write(decrypted_data)
