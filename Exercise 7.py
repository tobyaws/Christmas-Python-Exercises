from math import sqrt
from itertools import count, islice


def is_prime(num):
    if num < 2:
        return print("{0} is not a prime number".format(num))

    for number in islice(count(2), int(sqrt(num) - 1)):
        if num % number == 0:
            return print("{0} is not a prime number".format(num))

    return print("{0} is a prime number".format(num))


is_prime(int(input("Enter a number: ")))
