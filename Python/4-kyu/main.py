"""
In this kata you have to write a Morse code decoder for wired electrical telegraph.
Electric telegraph is operated on a 2-wire line with a key that, when pressed, connects the wires together,
which can be detected on a remote station. The Morse code encodes every character being transmitted as a sequence of "dots"
(short presses on the key) and "dashes" (long presses on the key).

When transmitting the Morse code, the international standard specifies that:

"Dot" – is 1 time unit long.
"Dash" – is 3 time units long.
Pause between dots and dashes in a character – is 1 time unit long.
Pause between characters inside a word – is 3 time units long.
Pause between words – is 7 time units long.

However, the standard does not specify how long that "time unit" is.
And in fact different operators would transmit at different speed.
An amateur person may need a few seconds to transmit a single character,
a skilled professional can transmit 60 words per minute, and robotic transmitters may go way faster.

For this kata we assume the message receiving is performed automatically by the hardware that checks the line periodically,
and if the line is connected (the key at the remote station is down), 1 is recorded, and if the line is not connected
(remote key is up), 0 is recorded. After the message is fully received, it gets to you for decoding as a string containing only symbols 0 and 1.

For example, the message HEY JUDE, that is ···· · −·−−   ·−−− ··− −·· · may be received as follows:

1100110011001100000011000000111111001100111111001111110000000000000011001111110011111100111111000000110011001111110000001111110011001100000011

As you may see, this transmission is perfectly accurate according to the standard, and the hardware sampled the line exactly two times per "dot".

That said, your task is to implement two functions:

Function decodeBits(bits), that should find out the transmission rate of the message, correctly decode the message to dots .,
 dashes - and spaces (one between characters, three between words) and return those as a string. Note that some extra 0's
   may naturally occur at the beginning and the end of a message, make sure to ignore them. Also if you have trouble
   discerning if the particular sequence of 1's is a dot or a dash, assume it's a dot.

2. Function decodeMorse(morseCode), that would take the output of the previous function and return a human-readable string.

NOTE: For coding purposes you have to use ASCII characters . and -, not Unicode characters.

The Morse code table is preloaded for you (see the solution setup, to get its identifier in your language).


Eg:
  morseCodes(".--") //to access the morse translation of ".--"
All the test strings would be valid to the point that they could be reliably decoded as described above,
so you may skip checking for errors and exceptions, just do your best in figuring out what the message is!

Good luck!

After you master this kata, you may try to Decode the Morse code, for real.
"""

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

def decode_bits(bits: str):
    bits = bits.strip("0")
    mess = ""
    rate = None
    one_count = 0
    zero_count = 0
    for digit in bits:
        if int(digit):
            if rate is None and zero_count:
                rate = min(zero_count, one_count)

            if zero_count:
                if zero_count<rate or one_count<rate:
                    mess = mess.replace(".", "-").replace("|", " ")
                    rate = min(zero_count, one_count)

                if one_count == rate:
                    mess += "."
                elif one_count == rate*3:
                    mess += "-"
                if zero_count == rate:
                    mess += "|"
                elif zero_count == rate*3:
                    mess += " "
                elif zero_count == rate*7:
                    mess += "   "
                one_count = 0
                zero_count = 0

            one_count += 1

        else:
            zero_count += 1

    if one_count:
        if rate and one_count == rate:
            mess += "."
        elif rate and one_count == rate*3:
            mess += "-"
        else:
            mess += "."
    return mess.replace("|", "")

def decode_morse(morseCode):
    mess = ""
    curr_seq = ""
    space_count = 0
    for char in morseCode.strip():
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

def solution(args):
    """
    A format for expressing an ordered list of integers is to use a comma separated list of either
    individual integers or a range of integers denoted by the starting integer separated from the
    end integer in the range by a dash, '-'. The range includes all integers in the interval including
    both endpoints. It is not considered a range unless it spans at least 3 numbers. For example "12,13,15-17"
    Complete the solution so that it takes a list of integers in increasing order and returns a correctly
    formatted string in the range format.
    """
    res = ""
    curr_seq = []
    last_num = None
    for num in args:
        if last_num is None:
            curr_seq.append(num)
        else:
            if num - last_num == 1:
                curr_seq.append(num)
            else:
                res += get_string(curr_seq)
                curr_seq = [num]
        last_num = num
    return res + get_string(curr_seq).rstrip(',')

def get_string(curr_seq):
    res = ""
    if len(curr_seq) < 3:
        for n in curr_seq:
            res += f"{n},"
    else:
        res += f"{curr_seq[0]}-{curr_seq[-1]},"
    return res

solution([-6,-3,-2,-1,0,1,3,4,5,7,8,9,10,11,14,15,17,18,19,20])