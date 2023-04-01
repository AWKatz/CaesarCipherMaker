# Day 8 of 100 for the Udemy Python Bootcamp

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def caesar(input_text, shift_value, cipher_direction):
    message_text = ""
    # Multiply by a negative to change direction of values
    if cipher_direction == "decode":
        shift_value *= -1
    for char in input_text:
        if char in alphabet:
            position = alphabet.index(char)
            new_position = position + shift_value
            message_text += alphabet[new_position]
        else:
            message_text += char
    print(f"The {cipher_direction} message is : {message_text}")


from art import logo
print(logo)
keep_alive = True

while keep_alive:

    direction = input("Type 'encode' to encrypt a message, type 'decode' to decrypt a message:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    # Use mod to ensure that the shift value is always kept within the range of alphabet
    shift = shift % 26

    caesar(input_text=text, shift_value=shift, cipher_direction=direction)

    user_input = input("\nType 'yes' if you want to rerun. Otherwise type 'no' to quit.\n")
    if user_input == 'no':
        keep_alive = False
        print("\nClearing cache, deleting files, purging database, resetting environment variables")
