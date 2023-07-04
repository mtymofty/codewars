# 1.
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

# 2.
def number(bus_stops):
    """
    There is a bus moving in the city which takes and drops some people at each bus stop.
    You are provided with a list (or array) of integer pairs. Elements of each pair represent
    the number of people that get on the bus (the first item) and the number of people that get
    off the bus (the second item) at a bus stop. Your task is to return the number of people who
    are still on the bus after the last bus stop (after the last array). Even though it is the last
    bus stop, the bus might not be empty and some people might still be inside the bus, they are probably
    sleeping there :D Take a look on the test cases. Please keep in mind that the test cases ensure that the
    number of people in the bus is always >= 0. So the returned integer can't be negative. The second value in
    the first pair in the array is 0, since the bus is empty in the first bus stop.
    """
    return sum(map(lambda pair: pair[0] - pair[1], bus_stops))