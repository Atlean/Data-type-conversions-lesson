"""Dictionary"""

"""We can create an empty dictionary."""

emptywords = {}

emptywords2 = dict()

"""Contains a value attached to a word."""

words = {'one':1,'two':2,'three':3,'four':4}

"""To access a key value in the dictionary, the key value is entered inside curly brackets and the value value is accessed."""

print(words['two'])

"""More than one value can be entered for a key value and these values can be accessed."""

words2 = { "a" : [1,2,3,4,5],"b" : [[1,2,3,4],[6,7,8],[9,11,23]], "c" : [99]  }

print(words2["b"][1][2]) ; """This print give us 8 from words2"""

"""We can also use operators in dictionaries."""

words2["c"][0] += 1

print(words2["c"][0])

"""Nested dictionaries can be written."""

nested = {"numbers":{"four":4,"six":6},"vegetablesandcolors":{"orange":"red","apple":"blue"}}

print(nested["numbers"]["six"])

print(nested["vegetablesandcolors"]["apple"])

"""Key values can be accessed individually or even both at the same time using various methods."""

new_dic = {"one":1,"four":4,"six":6}

print(new_dic["one"], new_dic["four"], new_dic["six"])

print(new_dic.keys())

print(new_dic.values())

print(new_dic.items())

