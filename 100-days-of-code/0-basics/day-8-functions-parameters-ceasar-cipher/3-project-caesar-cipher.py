from art import logo, image

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def caesar(start_text, shift_amount, cipher_direction):
    end_text = ""
    if cipher_direction == "decode":
        shift_amount *= -1
    for letter in start_text:
        if letter in letters:
            position = letters.index(letter)
            new_position = position + shift_amount
            if new_position >= len(letters):
                new_position -= len(letters)
            elif new_position < 0:
                new_position += len(letters)
            end_text += letters[new_position]
        else:
            end_text += letter
    print(f"The {cipher_direction}d text is {end_text}.")

print(logo)
print("Welcome to the Caesar Cipher!")
print(image)
should_continue = True
while should_continue:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n")) % 26
    caesar(start_text=text, shift_amount=shift, cipher_direction=direction)
    result = input("Type 'yes' if you want to go again. Otherwise type 'no'.\n")
    if result == "no":
        should_continue = False
        print("Goodbye!")
