# x = 5
# while x > 0:
#     print(x)
#     x = x-1
#("Next!")

# x = 5
# while x > 3:
#     print(x)
#     x = x-1
# print("Next!")


# x = 5
# while x > 0: #infinite loop!
#     print(x)
#     x+=1
# print("Next!")

# x = 1
# while x < 5:
#     print(x)
#     x+=1
# print("Stop!")

# x = 1
# while x < 5:
#     print(x)
#     if x == 3: # x breaks at 3
#         break
#     x+=1
# print("Stop!")


# x = 1
# while x < 5:
#     #print(x)
#     if x == 3:
#         break
#     #print(x)
#     x+=1
#     print(x)  # Here, x starts from 2 because x+=1 = 2
# print("Stop!")


# x = 1
# while x < 5:
#     #print(x)
#     if x == 3:
#         break
#     print(x) # Here, x starts from 1 because x = 1. x breaks at 2. Where you print is key to how the code runs
#     x+=1
#     #print(x)
# print("Stop!")

# n = 8
# num_div = 2
# while n != 1:
#     n = n/2
#     num_div += 1
# print(num_div)

# import random

# rnd = random.randint(1, 1000) 
# def master(x):
#     rnd = random.randint(1, 1000) 
#     while x != rnd: 
#         x = int(input(f"Guess a number between 1 and 1000: ")) 
#         if x > rnd:
#             return("Too low")
#         elif x < rnd:
#             return("Too high")
#     else:
#       return(f"Correct number {x}!")


# correct_pin = 1234
# wrong_attempts = 0
# while wrong_attempts < 5:    
#     entered_pin = int(input("Enter your pin: "))
#     if entered_pin == correct_pin:
#         print("Yes, you are the guy, logging you in!!")
#         break
#     wrong_attempts = wrong_attempts + 1


# current_battery_percentage = int(input("Enter current battery percentage: "))
# while current_battery_percentage < 15:
#     print("LOW BATTERY, PLEASE CHARGE")
#     current_battery_percentage = current_battery_percentage + 1



current_battery_percentage = 100
while current_battery_percentage >= 10:
    print(f"BATTERY NOT LOW: {current_battery_percentage}")
    current_battery_percentage -= 10
print("BATTERY LOW!!")
#print (f"BATTERY LOW : {current_battery_percentage}")


# current_battery_percentage = 100
# while current_battery_percentage >= 10:
#     print((current_battery_percentage))
#     current_battery_percentage -= 10
# print("BATTERY LOW")
