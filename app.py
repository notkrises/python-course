x = input("x: ")
y = int(x) + 1
"""
y = x + 1 # gives error bc adding an integer to a str

int(x) # converts into an int
str(x) # converts into a str
float(x) # converts into a float
bool(x) # converts into a bool (0, "", and None are False, everything else is True)"""

print(f"x: {x}, y: {y}")
