# .append , .extend

old_languages = ["c", "cpp"]
old_languages.append("java")

modern_languages = ["javascript", "python"]


old_languages.extend(modern_languages)

print(old_languages)


# .count, .index
votes = ["yes", "yes", "no", "no", "no", "no"]
print(votes.count("no"))
print(votes.index("no"))


# .clear

votes.clear()
old_languages.clear()
print(votes)
print(old_languages)

# Array copy -> .copy

list1 = ["apple", "banana", "papaya"]
# list2 = list1  # -> Shallow copy
list2 = list1.copy()  # -> deep copy

list2.append("grapes")

print("list 1 ==>>", list1)
print("list 2 ==>>", list2)
