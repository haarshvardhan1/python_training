# functions -> Set of instructions /Group of intructions

# Arugmemts & Paramters


# name -> parameter
def greet(name, *agrs, **kwagrs):
    print(f"Hello {name}! Welcome to python tutorials")


# Value is argument
greet("Harshvardhan", 26)
# greet("Naman")


def calculate_tax(subtotal):
    tax_amount = subtotal * 0.05
    return tax_amount


my_tax = calculate_tax(100.00)
total_bill = 100.00 + my_tax

print(f"My total bill is {total_bill} and taxes calculated are {my_tax}")


def apply_discount(price, discount: int = 0):
    final_price = price - discount
    return final_price


print("Price after discount => ", apply_discount("50.00", 10))
print("Price after discount => ", apply_discount(100))
