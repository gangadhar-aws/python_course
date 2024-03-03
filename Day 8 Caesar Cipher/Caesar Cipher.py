


alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p',
            'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def caesar(text, shift, direction):
    cipher_text = ""
    if direction == "encode":
        for letter in text:
            if letter in alphabet:
               possition = alphabet.index(letter)
               cipher_text += alphabet[possition+shift]
            else:
                cipher_text += letter
    elif direction == "decode":
        for letter in text:
            if letter in alphabet:
                possition = alphabet.index(letter)
                cipher_text += alphabet[possition - shift]
            else:
                cipher_text += letter
    else:
        print("Wrong Input Entered Try Again!")
    print(cipher_text)

game_on = True
while game_on:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    caesar(text, shift, direction)

    user = input("Type 'yes' if you want to go again. other type 'no'.")
    if user == "no":
        game_on = False


# def encrypt(txt, sft):
#     cipher_text = ""
#     for letter in txt:
#         possition = alphabet.index(letter)
#         cipher_text += alphabet[possition+sft]
#
#     print(cipher_text)
#
# def  decrypt(txt, sft):
#     text = ""
#     for letter in txt:
#         possition = alphabet.index(letter)
#         text += alphabet[possition-sft]
#     print(text)
#
# direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
# text = input("Type your message:\n").lower()
# shift = int(input("Type the shift number:\n"))





