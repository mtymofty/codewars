def square_digits(num: int) -> int:
    """
    Square every digit of a number and concatenate them.
    """
    # digits = [digit**2 for digit in str(num)]
    # return int("".join(digits))
    res = 0
    for digit in str(num):
        val = int(digit) ** 2
        res = res * (10**len(str(val))) + val
    return res

def square_digits(num):
    ret = ""
    for x in str(num):
        ret += str(int(x)**2)
    return int(ret)

