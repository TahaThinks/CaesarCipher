
direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

def encrypt(plain_text, shift_amount):
    encrypted_message = ''
    for letter in plain_text:
        new_value = chr(ord(letter) + shift_amount)
        encrypted_message += new_value
    print(f"The encoded message is {encrypted_message}")

def decrypt(plain_text, shift_amount):
    encrypted_message = ''
    for letter in plain_text:
        new_value = chr(ord(letter) - shift_amount)
        encrypted_message += new_value
    print(f"The encoded message is {encrypted_message}")


if direction == "encrypt":
    encrypt(text, shift)
else:
    decrypt(text, shift) 
