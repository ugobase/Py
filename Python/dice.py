import random

again = True
while again:
    rnd = random.randint(1,6)
    print(rnd)
    another_roll = input("Want to roll again? (y/n):")
    if another_roll == "y":
        continue
    else:
        break