
direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

def caeser (start_text, shift_amout, cipher_direction):
    end_text = ''
    if cipher_direction == 'decode': shift_amout *= -1
    for letter in start_text:
        new_value = chr(ord(letter) + shift_amout)
        end_text += new_value

    print(f"The {cipher_direction}d message is {end_text}")
    
caeser(text, shift, direction)

# def encrypt(plain_text, shift_amount):
#     encrypted_message = ''
#     for letter in plain_text:
#         new_value = chr(ord(letter) + shift_amount)
#         encrypted_message += new_value
#     print(f"The encoded message is {encrypted_message}")

# def decrypt(plain_text, shift_amount):
#     encrypted_message = ''
#     for letter in plain_text:
#         new_value = chr(ord(letter) - shift_amount)
#         encrypted_message += new_value
#     print(f"The encoded message is {encrypted_message}")


# if direction == "encrypt":
#     encrypt(text, shift)
# else:
#     decrypt(text, shift) 
