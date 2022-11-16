alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p',
            'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

from art import *
print(logo)

def caesar(plain_text, shift_amount, direction_value):
    new_text = ""

    for letter in plain_text:
        if letter not in alphabet:
            new_text += letter
        else:
            letter_index = alphabet.index(letter)
            if direction_value == "encode":
                shifted_index = letter_index + shift_amount
                if shifted_index > len(alphabet):
                    shifted_index %= len(alphabet)
                new_letter = alphabet[shifted_index]
                new_text += new_letter
            elif direction_value == "decode":
                shifted_index = letter_index - shift_amount
                if shifted_index < 0:
                    shifted_index %= len(alphabet)
                new_letter = alphabet[shifted_index]
                new_text += new_letter

    if direction_value == "encode":
        print(f"Here's the encoded result: {new_text}")
    elif direction_value == "decode":
        print(f"Here's the decoded result: {new_text}")

cipher_active = True
while cipher_active:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    caesar(plain_text=text, shift_amount=shift, direction_value=direction)
    repeat = input("Type 'yes' if you want to go again. Otherwise type 'no'.\n").lower()
    if repeat == "no":
        cipher_active = False
        print("Goodbye")
