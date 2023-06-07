"""The import string statement imports the string module in Python, which 
contains a collection of string constants and utility functions"""
import string 


"""The function takes a character(char) and a key as inputs, and returns
an encrypt character by shifting its ASCII code by the value of the key"""
def encrypt_char(char, key):
    if char in string.ascii_lowercase:
        shifted_code= ((ord(char) - 97 + key) % 26) + 97
    elif char in string.ascii_uppercase:
        shifted_code = ((ord(char) - 65 + key) % 26) + 65
    else:
        return char 
    shifted_char = chr(shifted_code)
    return shifted_char


"""This function takes a text string and a key as inputs, and returns
an encrypt version of the text using the Caesar cipher."""
def encrypt_caesar(text, key):
    encrypted_text = ""
    for char in text:
        encrypted_char = encrypt_char(char, key)
        encrypted_text += encrypted_char
    return encrypted_text


"""This function takes a ciphertext string and a key as inputs, and
returns a decrypted version of the text using the Caesar cipher"""
def decrypt_caesar(ciphertext, key):
    decrypted_text = ""
    for char in ciphertext:
        decrypted_char = encrypt_char(char, -key)
        decrypted_text += decrypted_char
    return decrypted_text


"""The main function calls two other functions with some predetermined
input arguments"""
def main():
  print(encrypt_caesar('Learning Python is Fun!', 3))
  print(decrypt_caesar('Ohduqlqj Sbwkrq lv Ixq!', 3))


if __name__ == "__main__":
  main()
