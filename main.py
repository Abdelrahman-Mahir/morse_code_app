# This's part of 100 Days of Code by Angela Yu
# This's a Morse code application
# The aim is to be able to code and decode messages as chosen by the user


# Letters to Morse Code Dict. Added space as a character
LETTER_MORSE_DICT = {'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.',
                     'F': '..-.', 'G': '--.', 'H': '....', 'I': '..', 'J': '.---', 'K': '-.-',
                     'L': '.-..', 'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-',
                     'R': '.-.', 'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--',
                     'X': '-..-', 'Y': '-.--', 'Z': '--..', '1': '.----', '2': '..---', '3': '...--',
                     '4': '....-', '5': '.....', '6': '-....', '7': '--...', '8': '---..', '9': '----.', '0': '-----',
                     ',': '--..--', '.': '.-.-.-', '?': '..--..', '/': '-..-.', '-': '-....-',
                     '(': '-.--.', ')': '-.--.-'}


# Encode Function
def encode_msg(message):
    encoded_text = ""
    for letter in message.upper().strip():
        if letter == " ":
            encoded_text += "  "
        else:
            encoded_text += LETTER_MORSE_DICT[letter] + " "
    return encoded_text


# Decode function

def decode_msg(message):
    i = 0  # This's a counter to keep track of the list index when searching for consecutive spaces.
    decoded_text = ""
    letters_list = message.split(" ")
    for letter in letters_list:
        if letter != "":
            for key, value in LETTER_MORSE_DICT.items():
                if letter == value:
                    decoded_text += key
        else:
            try:
                if letters_list[i + 1] == letter:
                    decoded_text += " "
            except:
                pass
        i += 1
    return decoded_text.capitalize()

print("Welcome to MORSE CODE APPLICATION. We can encode your secrets, or Decode hidden messages *___*")
is_on = True
while is_on:
    user_input = input(" Please Type 'Encode', 'Decode', or 'Close' ")
    if user_input.lower() == "encode":
        message = input("What's your message: ")
        encoded_text = encode_msg(message)
        print(f"The encoded message is:\n{encoded_text}")
    elif user_input.lower() == "decode":
        message = input("What's your message: ")
        decoded_text = decode_msg(message)
        print(f"The decoded message is:\n{decoded_text}")
    elif user_input.lower() == "close":
        print("Thank you for using our application :D")
        is_on = False
    else:
        print("Wrong input.")

