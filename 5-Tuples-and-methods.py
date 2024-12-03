"""Tuples"""

"""Tuples are created by enclosing them in parentheses."""

tuple1 = (2,4,6,8)

print(type(tuple1))

"""To access the indexes, we just need to use logic in the lists."""

print(tuple1[1])

"""To create a single-element tuple, place a comma after the index."""

tuple2 = (1,)

print(type(tuple2))

"""Tuples consist not only of numbers but also of strings."""

tuple3 = ("Arthur",)

print(type(tuple3))

"""Let's learn the count method. With the count method, we can find out how many elements there are in a tuple."""

"""This method is also used on tuples containing strings."""

tuple4 = (4,7,2,4,8,2,4,4,2,88,12,4,7,99,4)

print(tuple4.count(4)) ; """We see how many 4s there are."""

"""The index method is used to find which string a data is in."""

"""!!!Important note: First it shows which index it is in. 
It does not give the subsequent index numbers that have the same data."""

tuple5 = (7,2,4,8,2,4,4,2,88,12,4,7,99,4)

print(tuple5.index(4))

"""Indexes in tuples cannot be changed."""

"""
We can't write these codes: 

tuple6 = ("Apple","Banana","Orange")

tuple6[1] = "Lemon" ; It won't work.

tuple6.remove("Banana") ; It won't work

"""
"""Tuples are used if there is a part that you do not want to change. Another area of 
use is the data types that we call "read only". This way the program runs faster. 
Apart from this, we usually use lists."""