def reverse_cipher(text):
    return text[::-1]

def caesar_cipher(text, shift=3):
    encrypted = ""
    for char in text:
        if char.isalpha():
            offset = 65 if char.isupper() else 97
            encrypted += chr((ord(char) - offset + shift) % 26 + offset)
        else:
            encrypted += char
    return encrypted

def atbash_cipher(text):
    encrypted = ""
    for char in text:
        if char.isupper():
            encrypted += chr(90 - (ord(char) - 65))
        elif char.islower():
            encrypted += chr(122 - (ord(char) - 97))
        else:
            encrypted += char
    return encrypted