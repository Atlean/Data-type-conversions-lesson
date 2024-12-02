"""Lists can contain many types of data."""
list1 = [1,3.4,7,"Apple",28]

print(list1)

"""To find out the number of data in the list, the len function is used as in our previous courses."""

print(len(list1))

"""There are 2 ways to create only empty list:"""

emptylist1 = list()

emptylist2 = []

print(emptylist1)

print(emptylist2)

"""To find out the number of data in the list, the len function is used as in our previous courses."""

"""The list function is also used to separate letters in a sentence or word."""

list2 = list("Hello World")

print(list2)

"""We can pick the unit with the desired index number from a list."""

list3 = [2,5,9,12,16,7]

"""Index numbers start from 0 and continue. Now, since our 3rd index is 12, let's print the number 12."""

print(list3[3])

"""Index numbers can be (-) values. In this case, it starts from the end of the list and continues.
 For example, if we say -1 in list3, we reach 7, if we say -4, we reach 9."""

print(list3[-1])

print(list3[-4])

"""If we want to print the data up to the 2nd index, I need to print it as (::2). I will show this with other examples."""

print(list3[::2])

"""The ::-3 command also gives us the data starting from the back and skipping 3 by 3."""

print(list3[::-3])

"""Lists can be processed with some operators. For example, let's merge two lists."""

list4 = [1,2,3,4]

list5 = [5,6,7,8]

print(list4+list5)

"""Let's print a list 3 times."""

list6 = ["^-^"]

print(list6*3)

"""We can change units and refresh the list by specifying the index number."""

list7 = [3,56,79,2,35,111]

"""Let's change the number 35 in the 4th index to 328"""

list7[4] = 328

print(list7)

"""We can add data to a list with the append method. 
All added values are added to the end and create the last index."""

list8 = [2,4,6,8]

list8.append(1)

print(list8)

"""With the pop method, a value we want is extracted and given to us. 
If we do not give a value to pop, it extracts the last index.
After this value is extracted, the list remains extracted."""

list9 = [23,29,95,75,83,91,66]

list9.pop(3)

print(list9)

"""The sort method allows us to sort elements from smallest to largest or largest to smallest."""

list10 = [23,42,9,12,56,81,103]

"""from small to large(Cannot be used in print)"""

list10.sort()

print(list10)

"""from large to small(Cannot be used in print)"""

list10.sort(reverse=True)

print(list10)