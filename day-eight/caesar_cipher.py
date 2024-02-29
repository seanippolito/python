from art import logo

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def caesar_cipher(direction, text, shift):
    text = text.lower()
    if direction == "decode":
        shift *= -1
    text_list = list(text)
    for i in range(len(text_list)):
        if text_list[i] in alphabet:
            index = alphabet.index(text_list[i])
            text_list[i] = alphabet[(index + shift) % 26]
        else:
            continue
    return "".join(text_list)


print(logo)
continue_cipher = True
while (continue_cipher):
    print(caesar_cipher(input("Type 'encode' to encrypt, type 'decode' to decrypt: \n"), input("Type your message: \n"), int(input("Type the  shift number: \n"))))
    continue_cipher = input("Type 'y' if you want to go again. Otherwise type 'n': \n") == "y"

print("Goodbye!")