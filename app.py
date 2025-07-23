def increment(number, by=1):  # makes the argument 1 by default and optional
    return number + by
# all optional parameters should come AFTER required parameters


# keyword argument, not necessary but allows reader to know what it stands for
print(increment(2, by=5))  # second argument not needed
