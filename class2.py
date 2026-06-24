# Operators in python

a = 10
b = 2

# Arithmetic operators (+, -, *, /, // ,%, **)

print(a + b)
print(a - b)
print(a * b)
print(a / b)
print(10 / 3)  # 3.33
print(a // b)
print(10 // 3)  # 3
print(a % b)
print(10 % 3)
print(a**b)


#  Assigment operators ( = , +=, -=, *=  )
print("\nAssignemnt operators")
z = 10
print(z)

z += 2  # z = z + 2
print(z)

z -= 2  # z = z - 2
print(z)

z *= 2  # z = z * 2
print(z)


# Comparision operators ( ==, !=, >, <, >= ,<=) After comparison True or False (Boolean Values)
print("\nComparison operators")

print(a == b)
print(a != b)
print(a > b)
print(a < b)


# Logical Operators ( and, or , not)

# Identity and Membership operator / python magic  Membership(in , not in) Identity(is, is not)
fruits = ["apple", "banana", "mango"]
print("\n Membership")

compare = "cherry" in fruits
print(compare)
print("cherry" not in fruits)
