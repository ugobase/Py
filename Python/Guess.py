import random

# def game(x):
#     rnd = random.randint(1, x) # Random number between 1 and x
#     guess = 0             # guess = 0 and would never == rnd
#     while guess != rnd:    # Condition telling that guess != rnd
#         guess = int(input(f"Guess a number between 1 and {x}: "))  # Everything indented tells that guess != rnd
#         if guess < rnd:
#             print("Too Low")
#         elif guess > rnd:
#             print("Too High")
#     print(f"You got the number {rnd}")  # Here, guess == rnd

# game (10)

# def game(x):
#     rnd = random.randint(1, 9) 
#     guess = 7            # Guess could be any number 
#     while guess != rnd:   # Condition telling that guess is not rnd but when it is, there'd be a change
#         guess = int(input(f"Guess a number between 1 and {x}: "))  
#         if guess > rnd:
#             print("Too high")
#         elif guess < rnd:
#             print("Too Low")
#     else:
#       print(f"Correct number {rnd}!")
    
# game (10)


# def game(x):
#     rnd = random.randint(1, 10) 
#     #guess = 7            # Guess could be any number 
#     while x != rnd:   # Condition telling that guess is not rnd but when it is, there'd be a change
#         x = int(input(f"Guess a number between 1 and 10: "))  
#         if x > rnd:
#             print("Too high")
#         elif x < rnd:
#             print("Too Low")
#     else:
#       print(f"Correct number {rnd}!")
    
# game (6)


# def base(x):
#     low = 1
#     high = x
#     feedback = "a"   # Here, feedback = a
#     while feedback != "c":    # Condition telling that feedback is not c but when it is c, there'd be a change
#          if low != high:
#             guess = random.randint(low, high)
#          else:
#              guess = low  # Guess is between 1 and x
#          feedback = input(f"is {guess} too high (H), too low (L) or correct (C)? ")
#          if feedback == "h":  # If feedback is (h), x = guess(random integer) - 1
#             high = guess - 1
#          elif feedback == "l":  # If feedback is (l), l = guess(random integer) + 1
#             low = guess + 1
#     print(f"Computer guessed your number, {guess} correctly")   

# base(10)


# def base(x):
#     low = 1
#     high = 10
#     feedback = "a"   # Here, feedback = a
#     while feedback != "c":    # Condition telling that feedback is not c but when it is c, there'd be a change
#          if low != high:
#             guess = random.randint(low, high)
#          else:
#              guess = low  # Guess is between 1 and x
#          feedback = input(f"is {guess} too high (H), too low (L) or correct (C)? ")
#          if feedback == "h":  # If feedback is (h), x = guess(random integer) - 1
#             high = guess - 1
#          elif feedback == "l":  # If feedback is (l), l = guess(random integer) + 1
#             low = guess + 1
#     print(f"Computer guessed your number, {guess} correctly")   

# base(10)


#rnd = random.randint(1, 1000) 
def game_master(x):
    rnd = random.randint(1, 10)
    while x != rnd: 
        x = int(input(f"Guess a number between 1 and 10: ")) 
        if x > rnd:
            print("Lower!")
            #x-=1
        elif x < rnd:
            print("Higher!")
            #x+=1
    else:
      print(f"Correct number {x}!")

game_master(5)