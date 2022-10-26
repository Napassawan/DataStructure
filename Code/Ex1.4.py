print("*** Fun with Drawing ***")
j = int(input("Enter input : "))
r = 2 * j - 2
for i in range(-r, r + 1):
    for j in range(-r, r + 1):
        if abs(j) + abs(i) == abs(j) * 2 and j % 2 == 0:
            print("#", end="")
        elif abs(j) + abs(i) == abs(j) * 2 and j % 2 == 1:
            print(".", end="")
        elif abs(i) % 2 == 1 and abs(j) % 2 == 1:
            print(".", end="")
        elif abs(i) % 2 == 0 and abs(j) % 2 == 0:
            print("#", end="")
        elif abs(i) % 2 == 1 and abs(j) % 2 == 0 and abs(i) < abs(j):
            print("#", end="")
        elif abs(i) % 2 == 0 and abs(j) % 2 == 1 and abs(i) < abs(j):
            print(".", end="")
        elif abs(i) % 2 == 1 and abs(j) % 2 == 0 and abs(i) > abs(j):
            print(".", end="")
        elif abs(i) % 2 == 0 and abs(j) % 2 == 1 and abs(i) > abs(j):
            print("#", end="")
        else:
            print(" ", end="")

    print()