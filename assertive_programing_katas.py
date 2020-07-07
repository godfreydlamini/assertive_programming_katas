MORSE_CODE_DICT = {'A':'.-', 'B':'-...', 
		           'C':'-.-.', 'D':'-..', 'E':'.', 
		           'F':'..-.', 'G':'--.', 'H':'....', 
		           'I':'..', 'J':'.---', 'K':'-.-', 
		           'L':'.-..', 'M':'--', 'N':'-.', 
		           'O':'---', 'P':'.--.', 'Q':'--.-', 
		           'R':'.-.', 'S':'...', 'T':'-', 
		           'U':'..-', 'V':'...-', 'W':'.--', 
		           'X':'-..-', 'Y':'-.--', 'Z':'--..', 
		           '1':'.----', '2':'..---', '3':'...--', 
		           '4':'....-', '5':'.....', '6':'-....', 
		           '7':'--...', '8':'---..', '9':'----.', 
		           '0':'-----', ', ':'--..--', '.':'.-.-.-', 
		           '?':'..--..', '/':'-..-.', '-':'-....-', 
		           '(':'-.--.', ')':'-.--.-'}

def letters_to_morse_code(text):
    morse_code = ' '
    for letter in text:
        if letter != ' ':
            morse_code += MORSE_CODE_DICT[letter] + ' '
        else:
            morse_code += ' /'
    return morse_code

def morse_code_to_letters(text):
    text += ' '
    decrypt = ''
    encrypted_text = ''
    for letter in text:
        if (letter != ' '):
            counter = 0
            encrypted_text += letter
        else:
            counter += 1
            if counter == 2:
                decrypt += ' '
            else:
                decrypt += list(MORSE_CODE_DICT.keys())[list(MORSE_CODE_DICT.values()).index(encrypted_text)]
                encrypted_text = ''

    return decrypt
    
def main():
    text = "Hi there"
    cipher = letters_to_morse_code(text.upper())
    assert len(text) != 0, 'You cannot encrypt a blank text'
    print("Original message:",text)
    print("Message in Morse Code:",cipher)
    print("Message length:",len(text))
  
    text = ".... ..  - .... . .-. ."
    text_length =list(text.split(' '))
    cipher = morse_code_to_letters(text)
    assert len(text) != 0, 'You cannot decrypt a blank text'
    print("\nMorse Code:",text)
    print("Message in plain text:",cipher)
    print(f"Message length: {len(text_length)}")

if __name__ == "__main__":
    main()