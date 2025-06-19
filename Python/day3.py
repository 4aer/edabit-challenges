'''
def find_perimeter(width, length):
    return (width + length) * 2

print(find_perimeter(10, 20))
'''

# Create a function that takes two strings as arguments and returns the number of times the first string (the single character) is found in the second string.

def char_count(txt1, txt2):
    return txt2.count(txt1)

print(char_count("OH", "OHIO"))