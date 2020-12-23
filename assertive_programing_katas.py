 
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
		           '0':'-----', ' ': '/'}

def letters_to_morse_code(text):
    morse_code = ' '
    for letter in text:
        if letter != ' ':
            morse_code += MORSE_CODE_DICT[letter] + ' '
        else:
            morse_code += ' / '
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
            if letter == '/':
                decrypt += ' '
            else:
                decrypt += list(MORSE_CODE_DICT.keys())[list(MORSE_CODE_DICT.values()).index(encrypted_text)]
                encrypted_text = ''

    return decrypt
    
def main():
    text = "Hi there"
    result_to_code = letters_to_morse_code(text.upper()) 
    assert len(text) !=0, "The number of spaces should be the same"
    print("Original message:",text)
    print("Message in Morse Code:",result_to_code)
    print("Message length:",len(text))
  
    text = ".... .. / - .... . .-. ."  
    text_length =list(text.split(' '))
    result_to_letters = morse_code_to_letters(text)
    assert result_to_code != result_to_letters, "The number of characters should be the same"
    print("\nMorse Code:",text)
    print("Message in plain text:",result_to_letters)
    print(f"Message length: {len(text_length)}")

if __name__ == "__main__":
    main()
