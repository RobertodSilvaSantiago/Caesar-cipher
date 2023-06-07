# Caesar-cipher

This code demonstrates the implementation of the Caesar cipher encryption and decryption algorithms in Python. Here's how the code works:

The string module is imported, which contains various string constants and utility functions.

The encrypt_char function takes a character (char) and a key as inputs. It checks if the character is a lowercase or uppercase letter using the string.ascii_lowercase and string.ascii_uppercase constants. If it is a letter, it calculates the shifted ASCII code by adding the key to the character's ASCII code. The modulo operator (%) is used to ensure that the shifted code remains within the range of lowercase or uppercase letters. The shifted ASCII code is then converted back to a character using the chr function and returned. If the character is not a letter, it is returned as is.

The encrypt_caesar function takes a text string and a key as inputs. It initializes an empty string, encrypted_text, to store the encrypted version of the text. It iterates over each character in the text and calls the encrypt_char function to encrypt the character using the given key. The encrypted character is then appended to the encrypted_text string. Once all characters have been encrypted, the encrypted_text string is returned.

The decrypt_caesar function takes a ciphertext string and a key as inputs. It works similarly to the encrypt_caesar function, but it calls the encrypt_char function with a negative key to decrypt the characters. The decrypted characters are appended to the decrypted_text string, which is returned once all characters have been decrypted.

The main function serves as the entry point of the program. It calls the encrypt_caesar function with the input text "Learning Python is Fun!" and a key of 3, and then prints the encrypted text. It also calls the decrypt_caesar function with the input ciphertext "Ohduqlqj Sbwkrq lv Ixq!" and a key of 3, and prints the decrypted text.

Finally, the main function is executed when the script is run, as indicated by the if __name__ == "__main__" condition.

Overall, this code demonstrates a basic implementation of the Caesar cipher encryption and decryption algorithms using the ASCII representation of characters.
