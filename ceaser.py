def encrypt(plaintext, shift):
    """Encrypt the plaintext using Caesar Cipher with the given shift."""
    encrypted_text = ""
    for char in plaintext:
        if char.isalpha():
            # Shift the character
            shift_base = 65 if char.isupper() else 97  # 'A' or 'a'
            encrypted_char = chr((ord(char) - shift_base + shift) % 26 + shift_base)
            encrypted_text += encrypted_char
        else:
            # Non-alphabet characters are added without changes
            encrypted_text += char
    return encrypted_text


def decrypt(ciphertext, shift):
    """Decrypt the ciphertext using Caesar Cipher with the given shift."""
    decrypted_text = ""
    for char in ciphertext:
        if char.isalpha():
            # Shift the character back
            shift_base = 65 if char.isupper() else 97  # 'A' or 'a'
            decrypted_char = chr((ord(char) - shift_base - shift) % 26 + shift_base)
            decrypted_text += decrypted_char
        else:
            # Non-alphabet characters are added without changes
            decrypted_text += char
    return decrypted_text


def main():
    print("Welcome to the Caesar Cipher program!")
    action = input("Would you like to (E)ncrypt or (D)ecrypt a message? ").strip().lower()

    if action not in ['e', 'd']:
        print("Invalid choice. Please choose 'E' to encrypt or 'D' to decrypt.")
        return

    text = input("Enter the message: ")
    shift = int(input("Enter the shift value (between 1 and 25): "))

    # Ensure shift value is between 1 and 25
    if shift < 1 or shift > 25:
        print("Shift must be between 1 and 25. Please try again.")
        return

    if action == 'e':
        encrypted_message = encrypt(text, shift)
        print(f"\nEncrypted message: {encrypted_message}")
    else:
        decrypted_message = decrypt(text, shift)
        print(f"\nDecrypted message: {decrypted_message}")


if __name__ == "__main__":
    main()
