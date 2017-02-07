import cs50

while True:
    height = cs50.get_int()
    if height <= 23 or height >= 0 or height is None:
        break
    print("Invalid, please try again.")
    
for i in range(height):
    i += 1
    for j in range(height-i):
        print(" ", end="")
    for k in range(i):
        print("#", end="")
    print("  ", end="")
    for k in range(i):
        print("#", end="")
    print()