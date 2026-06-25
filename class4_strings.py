#  Strings
# sequence of character wrapped around quote

course = "Python"

# P     Y   T   H   O   N
# 0     1   2   3   4   5
# -6    -5  -4   -3   -2   -1
# Indexing and splicing


# print(course[2])
# print(course[-2])

# Splicing
# string[start:end:step] by default start 0, end -> length of string, step -> 1
# print(course[::-1])


# String methods
# .lower() / .upper()
# .strip()
# replace(old, new)
# split()

print(course.lower())
print(course.upper())


string = "  I love python.  "
print(string.strip())
print(string.strip().split(" "))


print(string.replace("love", "hate"))
