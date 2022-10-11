from cgitb import reset
import string

def bool_to_word(_boolean):
    return "Vrai" if _boolean else "Faux"


def count_true_booleans(array):
    counter = 0
    for boolean in array:
        if boolean:
            counter += 1
    return counter
#    return array.count(True)

_bools = [True, False, True, True, False, True, False, True, True, False]


def high_and_low(numbers):
    nbrs = [int(x) for x in numbers.split()]
    return f"{max(nbrs)} {min(nbrs)}"

def high_and_low(numbers):
    split_nbrs = numbers.split()

    res = []
    for num in split_nbrs:
        res.append(int(num))
    
    _min = min(res)
    _max = max(res)

    return f"{_max} {_min}"

def make_upper_case(s):
    return s.upper()


def reverse(string):
    return string[::-1]


def double(i):
    return i * 2


def alphabet_position(text):
    text = text.lower()
    alpha = string.ascii_lowercase
    
    res = ''
    
    for letter in text:
        if letter.isalpha():
            res += f"{alpha.index(letter) + 1} "

    return res


def every_other_letter(word):
    res = ''
    for _index, letter in enumerate(word):
        if _index % 2 == 0:
            res += letter.lower()
        else:
            res += letter.upper()
    
    return res


def calculate_like_a_blond(num1, num2):
    num1, num2 = str(num1), str(num2)
    if len(num1) > len(num2):
        num2 = num2.zfill(len(num1))
    elif len(num2) > len(num1):
        num1 = num1.zfill(len(num2))

    result = []

    for i in range(len(num1)):
        result.append(str(int(num1[i]) + int(num2[i])))

    return "".join(result)













def alphabet_position(text):
    alphabet = string.ascii_lowercase
    return ' '.join([f"{alphabet.index(letter) + 1}" for letter in text.lower() if letter in alphabet])

def alphabet_position(text):
    return ' '.join(str(ord(c) - 96) for c in text.lower() if c.isalpha())


def even_or_odd(number):
    return "Pair" if number % 2 == 0 else "Impair"


def milliseconds(h, m, s):
    return 3600000 * h + 60000 * m + 1000 * s


def dna_to_rna(dna):
    return dna.replace('T', 'U')
