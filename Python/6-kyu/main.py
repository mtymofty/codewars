# 1.
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


# 2.
def is_valid_walk(walk: list):
    """
    You live in the city of Cartesia where all roads are laid out in a perfect grid.
    You arrived ten minutes too early to an appointment, so you decided to take the
    opportunity to go for a short walk. The city provides its citizens with a Walk
    Generating App on their phones -- everytime you press the button it sends you an
    array of one-letter strings representing directions to walk (eg. ['n', 's', 'w', 'e']).
    You always walk only a single block for each letter (direction) and you know it
    takes you one minute to traverse one city block, so create a function that will
    return true if the walk the app gives you will take you exactly ten minutes
    (you don't want to be early or late!) and will, of course, return you to your
    starting point. Return false otherwise.

    Note: you will always receive a valid array containing a random assortment of direction letters
    ('n', 's', 'e', or 'w' only). It will never give you an empty array (that's not a walk, that's standing still!).
    """
    return True if (walk.count('n') - walk.count('s') == 0 and walk.count('w') - walk.count('e') == 0 and len(walk) == 10) else False

# 3.
def dig_pow(n, p):
    """
    Given a positive integer n written as abcd... (a, b, c, d... being digits) and a positive integer p
    we want to find a positive integer k, if it exists, such that the sum of the digits of n taken to the successive powers of p is equal to k * n.

    In other words:
    Is there an integer k such as : (a ^ p + b ^ (p+1) + c ^(p+2) + d ^ (p+3) + ...) = n * k
    """
    num = 0
    for dig in str(n):
        num += int(dig) ** p
        p += 1

    num = num/n
    return num if type(num) is int or type(num) is float and num.is_integer() else -1

dig_pow(89, 1)