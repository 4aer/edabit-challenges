# 1. In this challenge, a farmer is asking you to tell him how many legs can be counted among all his animals. The farmer breeds three species:

# chickens = 2 legs
# cows = 4 legs
# pigs = 4 legs

# The farmer has counted his animals and he gives you a subtotal for each species. You have to implement a function that returns the total number of legs of all the animals.
'''
def animals(chickens, cows, pigs):
	return (chickens * 2) + (cows * 4) + (pigs * 4)

print(animals(6, 17, 25))
'''

# 2. Create a function that takes a string and returns it as an integer.
'''
def string_int(txt):
    return int(txt)
print("Trying this shit out: ", int(string_int(12.34)))
'''

# 3. Make this bool print false
# Before
'''
print(bool("Hello"))
print(bool(15))

# After
print("Try: ", (bool("")))
print("Try: ", (bool(0)))
'''
# 4. Learn how bool and str differ
'''
def bool_to_string(flag):
	return bool(flag)

print(type(bool_to_string(False)))

def bool_to_string(flag):
	return str(flag)

print(type(bool_to_string(False)))

# Type conversions functions
print(int("10"))        # 10
print(float("3.14"))    # 3.14
print(list("abc"))      # ['a', 'b', 'c']
print(bool(""))         # False
print(set([1, 2, 2]))    # {1, 2}
print(dict([("a", 1)]))  # {'a': 1}
print(chr(65))          # 'A'
print(ord('A'))         # 65
print(bin(7))           # '0b111'

'''

# 5. Create a function that takes a number as an argument, increments the number by +1 and returns the result.
'''
def addition(num):
	return (num + 1)

print(addition(1))
'''