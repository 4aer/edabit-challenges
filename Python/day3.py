'''
def find_perimeter(width, length):
    return (width + length) * 2

print(find_perimeter(10, 20))
'''

# Create a function that takes two strings as arguments and returns the number of times the first string (the single character) is found in the second string.
'''
def char_count(txt1, txt2):
    return txt2.count(txt1)

print(char_count("OH", "OHIO"))
'''

# You are given 2 out of 3 angles in a triangle, in degrees.

# Write a function that classifies the missing angle as either "acute", "right", or "obtuse" based on its degrees.

# An acute angle is less than 90 degrees.
# A right angle is exactly 90 degrees.
# An obtuse angle is greater than 90 degrees (but less than 180 degrees).
# For example: missing_angle(11, 20) should return "obtuse", since the missing angle would be 149 degrees, which makes it obtuse.

def missing_angle(angle1, angle2):
    total = 180
    missing = total - angle1 - angle2
    if missing:
        return "acute"
    elif missing == 90:
        return "right"
    else:
        return "obtuse"
    
print(missing_angle(100, 20))