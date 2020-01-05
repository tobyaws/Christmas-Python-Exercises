def celsius(f):
    return print(round(((f - 32) * 5 / 9)), end="°c\n")


f = int(input("Enter a temperature in Fahrenheit: "))
celsius(f)


def fahrenheit(c):
    return print(round(((9 * c) / 5 + 32)), end="°f\n")


c = int(input("Enter a temperature in Celsius: "))
fahrenheit(c)
