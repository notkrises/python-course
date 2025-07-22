course = "  Python Programming   "

# creates a NEW string that is upper_case, the original string is not affected
course_capital = course.upper()
# creates a a lower case string
course_lowercase = course.lower()
# capitalizes the first letter of every word
course_title = course.title()
# strips the useless spaces in a str
course_stripped = course.strip()
print(course.rstrip())  # strips the end
print(course.lstrip())  # strips the beginning\

# finds the index of when "Pro" shows up, and IS case-sensitive
print(course.find("Pro"))
print(course.replace("P", "J"))  # replaces all instances of "P" with "J"
# returns a boolean compared to find which returns an index
print("pro" in course)
print("swift" not in course)  # returns true bc swift is not in course

print(course.upper())
