"""All information we receive from the user is in string form. Numbers are also received from the user as strings."""

number = 43

number = float(number)

print(number)

"""Also we can mention the number inside of the float order."""

print(float(-7))

"""Besides, we can convert a float number to an integer, but in this process the decimal part is lost."""

number2 = 3.14

print(int(number2))

"""Numbers (int or float) can convert to strings."""

print(str(320))

number3convfromint = str(214)

"""len give us the length of str"""

print(len((number3convfromint)))

"""Strings can not be integer if they include letter or any character inside of it."""

wrongcodenumber = "4532asd"

"""So we can not turn this string to integer or float."""

"""If the string follows the mathematical rules, we can convert it to a float number."""

number4str = "6.395"

number5 = float(number4str)

print(number5)
