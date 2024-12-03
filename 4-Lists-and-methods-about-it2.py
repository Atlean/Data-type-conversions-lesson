"""We can also sort words alphabetically with the sort method."""

list1 = ["morgan","arthur","lemon","banana","purple"]

list1.sort()

print(list1)

"""We can keep a list inside another list. This will be useful for important topics like matrix in the future."""

list2 = [[23,14,25],[38,112,9],[99,1,85]]

print(list2)

"""Let's learn how to print the number 112 in Listing 2 to the terminal."""

print(list2[1][1])

"""We can combine separate lists into a single list."""

list3 = [22,38]

list4 = [102,89]

list5 = [3,77]

newlist = [list3,list4,list5]

print(newlist)