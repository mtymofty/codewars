# 1.
def find_needle(haystack):
    """
    Write a function findNeedle() that takes an array full of junk but containing one "needle"
    After your function finds the needle it should return a message (as a string) that says:
    "found the needle at position " plus the index it found the needle
    """
    for i, elem in enumerate(haystack):
        if elem == "needle":
            return f"found the needle at position {i}"

def find_needle(haystack):
    return f'found the needle at position {haystack.index("needle")}'


# 2.
def opposite(number):
    """
    Very simple, given an integer or a floating-point number, find its opposite.
    """
    return -number

def positive_sum(arr):
    """
    You get an array of numbers, return the sum of all of the positives ones.
    """
    return sum(n for n in arr if n > 0)


# 3.
def grow(arr):
    """
    Given a non-empty array of integers, return the result of multiplying the values together in order.
    """
    res = 1
    for num in arr:
        res = res * num

    return res


# 4.
def century(year):
    """
    Given a year, return the century it is in.
    """
    return year//100 if year%100 == 0 else year//100+1


# 5.
def smash(words):
    """
    Write a function that takes an array of words and smashes them together into a sentence and returns the sentence.
    You can ignore any need to sanitize words or add punctuation, but you should add spaces between each word.
    Be careful, there shouldn't be a space at the beginning or the end of the sentence!
    """
    return " ".join(words)








