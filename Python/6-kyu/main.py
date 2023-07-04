MORSE_CODE = {
    '.-': 'A', '-...': 'B', '-.-.': 'C', '-..': 'D', '.': 'E', '..-.': 'F',
    '--.': 'G', '....': 'H', '..': 'I', '.---': 'J', '-.-': 'K', '.-..': 'L',
    '--': 'M', '-.': 'N', '---': 'O', '.--.': 'P', '--.-': 'Q', '.-.': 'R',
    '...': 'S', '-': 'T', '..-': 'U', '...-': 'V', '.--': 'W', '-..-': 'X',
    '-.--': 'Y', '--..': 'Z',
    '-----': '0', '.----': '1', '..---': '2', '...--': '3', '....-': '4',
    '.....': '5', '-....': '6', '--...': '7', '---..': '8', '----.': '9',
    '.-.-.-': '.', '--..--': ',', '..--..': '?', '.----.': "'", '-.-.--': '!',
    '-..-.': '/', '-.--.': '(', '-.--.-': ')', '.-...': '&', '---...': ':',
    '-.-.-.': ';', '-...-': '=', '.-.-.': '+', '-....-': '-', '..--.-': '_',
    '.-..-.': '"', '...-..-': '$', '.--.-.': '@', '...---...': 'SOS'
}

def decode_morse(morse_code: str):
    """
    A simple Morse code decoder.
    """
    mess = ""
    curr_seq = ""
    space_count = 0
    for char in morse_code.strip():
        if space_count == 3:
            space_count = 0
            mess += " "
        if char != " ":
            curr_seq += char
            space_count = 0
        elif space_count == 0:
            mess += MORSE_CODE[curr_seq]
            curr_seq = ""
            space_count += 1
        elif space_count != 3:
            space_count += 1
    if curr_seq:
        mess += MORSE_CODE[curr_seq]
    return mess

def decodeMorse(morse_sequence):
    words = []
    for morse_word in morse_sequence.strip().split('   '):
        word = ''.join(MORSE_CODE.get(morse_char, '') for morse_char in morse_word.split(' '))
        if word:
            words.append(word)
    return ' '.join(words)


