#  if, else, elif

# Example
# Traffic lights, Green -> go, Yellow -> slow down, Red -> stop

# light = "red"

# if light == "green":
# # if True:
#     print("GO")
# elif light == "yellow":
#     print("Slow down and check for traffic")
# else:
#     print("Stop")


# Match
light = "blue"

match light:
    case "green":
        print("GO")
    case "yellow":
        print("Slow down and check for traffic")
    case "red":
        print("Stop")
    case _:
        print("Allowed values are red, green and yellow")
