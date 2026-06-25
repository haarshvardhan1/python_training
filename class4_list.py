# List -> []

cart = ["milk", "bread"]

cart.append("eggs")
cart.insert(1, "butter")
cart.remove("bread")
cart.pop()
print(cart)


# Tuples -> ()
cart1 = ("milk", "bread")
# index and count
print(cart1.count("milk"))

coordinates = (40.37645, -73.045738)
lat, lon = coordinates  # unpaking of a tuple
print(f"Latitude: {lat}, Longitide: {lon}")


# Dictionaries -> key value pairs/map {key1: value1, key2: value2} / JSON

student = {"name": "John", "grade": "A", "age": 23}
print(student["age"])
