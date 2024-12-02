"""Print, type and formatting functions (Bonus \n, \t , seperating, *)"""

"""The print() function in Python shows information on the screen(terminal). It is often used to check what the program is doing or to show messages to the user."""

print("Hello World")

print("Arthur Morgan")

"""Also you can use some operators inside of it."""

number1 = 5

number2 = 7

print(number1+number2)

"""We can print integers, numbers and floats at the same time with comma."""

print(32,3.56,"John")

"""If we want to write words under each other in a sentence, we use {\n}."""

print("Arthur\nMorgan")

"""If we want to leave a space between characters as long as a tab (press space 4 times), {\t} is used."""

print("Sunday\tMonday\tTuesday")

"""The Type function tells us what type the code on the screen is. This is a very important function."""

name = "Arthur"

print(type(name)) ; """It says it belongs to the string class."""

number3 = 72

print(type(number3)) ; """It says it belongs to the integer class."""

number4 = 43.56

print(type(number4)) ; """It says it belongs to the float class."""

"""Now we will learn how we seperate the sentences with print function.
We add * or / between all numbers with sep after the comma inside of the print function."""

print(1,4,6,8,9,sep="*")

print("06","10","2000",sep="/")

"""We observe that we can use \n in separate strings. We will also observe that when we use more than one \n, we skip more lines."""

print("Arthur","Morgan",sep="\n\n\n")

"""Now, let's use (*) before the word.It will open the space between each letter. Only the parameter with the star (*) is affected by this situation"""

print(*"Arthur")

print(*"Arthur", "Morgan")

"""We can combine sep and star(*)."""

print(*"FBI",sep=".")

print(*"LAPD",sep=".")

"""In Python, formatting means organizing text and combining variables with strings 
to make the output clear and easy to read. It helps create custom messages or show data in a specific way."""

"""Here I gave the a and b parameters to the curly brackets with the format function."""

a = 5
b = 3

print("{} minus {} is {}".format(a,b,a-b))

"""I can also decide what parameters to give to the curly brackets."""

print("{1} {0} {2} {3}".format("are","you","a","human"))

"""I can also decide how many digits the floats in the curly brackets will show. 
However, in this process, the rightmost digit is rounded to the nearest integer."""

print("{1:.1f} {0:.2f} {2:.2f} {3:.3f}".format(3.753,2.5743,7.32583,9.4591))
