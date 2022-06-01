def caesar_cipher(text):
    encrypted_message = ""
    for char in text:
        encrypted_message += chr(ord(char) + 3)
    return encrypted_message


message = input()

print(caesar_cipher(message))