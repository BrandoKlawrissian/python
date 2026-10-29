#Day 3 Python Coding: Conditional Statements, Logical Operators, Code Blocks and Scope
# if condition:
#     do this
# else:
#     do this
   
water_level = 50

if water_level > 80:
    print("drain water")
else:
    print("Continue")
   
# Task 1
print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))
 
if height >= 120:
    print("You can ride the rollercoaster")
else:
    print("You CANNOT ride the rollercoaster") 

#Task 2
#Pause 1    
# % or modulo operator, it goes between two numbers and calculates the remainder --> 10 % 5 = 2 / 10 % 3 = 1

#Pause 2
#Check odd or even
number = int(input("What is the number that you want to check?"))
 
if number % 2 == 0:
    print("Even")
else:
    print("Odd")

#Nested if statements and elif statements
# if condition:
#     if another condition:
#         do this
#     else:
#         do this
# else:
#     do this 

if height >= 120:
    print("You can ride the rollercoaster")
    age = int(input("What is your age? "))
    if age < 12:
        print("Please pay $5.")
    elif age < 18 :
        print("Please pay $7.")
    else:
        print("Please pay $12.")
else:
    print("You CANNOT ride the rollercoaster")  

#Coding Challenge BMI Calculator with Interpretations
weight = 85
height = 1.85

bmi = weight / (height ** 2)

if bmi < 18.5:
    print("underweight")
elif bmi > 25:
    print("overweight")
else:
    print("normal weight")   

#Multiple If statements in Succession
# if condition1:
#     do A
# if condition2:
#     do B
# if condition3:
#     do C 

print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))    
bill = 0

if height >= 120:
    print("You can ride the rollercoaster")
    age = int(input("What is your age? "))
    if age < 12:
        bill = 5
        print("Please pay $5.")
    elif age < 18 :
        bill = 7
        print("Please pay $7.")
    else:
        bill = 12
        print("Please pay $12.") 

    wants_photo = input("Do you want a photo taken? Type y for Yes or n for No.")
    if wants_photo == "y":
        bill += 3
    print(f"Your final bill is ${bill}")     
else:
    print("You CANNOT ride the rollercoaster")

#Pizza Order practice
#Task 5
print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M or L?: ")
pepperoni = input("Do you want pepperoni on your pizza? Y or N: ")
extra_cheese = input("Do you want extra cheese? Y or N: ")

small_pizza = 15
medium_pizza = 20
large_pizza = 25

add_pepperoni_small = 2
add_pepperoni_medium = 3
add_pepperoni_large = 3
add_pepperoni_medium_or_large = 3

add_extra_cheese = 1

bill = 0

if size == "S":
    bill += small_pizza
    if pepperoni == "Y":
        bill += add_pepperoni_small
    if extra_cheese == "Y":
        bill += add_extra_cheese
elif size == "M":
    bill += medium_pizza
    if pepperoni == "Y":
        bill += add_pepperoni_medium
    if extra_cheese == "Y":
        bill += add_extra_cheese
elif size == "L":
    bill += large_pizza
    if pepperoni == "Y":
        bill += add_pepperoni_large
    if extra_cheese == "Y":
        bill += add_extra_cheese
else:
    print("Invalid entry detected. Pizza will not be made")

if size in ("S", "M", "L"):
    print(f"Your final bill is: ${bill}.")

#todo: work out how much they need to pay based on their size choice.
if size == "S":
    bill += small_pizza
elif size == "M":
    bill += medium_pizza
elif size == "L":
    bill += large_pizza
else:
    print("Invalid entry detected. Pizza will not be made")

#todo: work out how much to add to their bill based on their pepperoni choice.
if pepperoni == "Y":
    if size == "S":
        bill += add_pepperoni_small
    else:
        bill += add_pepperoni_medium_or_large

#todo: work out their final amount based on whether if they want extra cheese.
if extra_cheese == "Y":
    bill += add_extra_cheese  

print(f"Your final bill is: ${bill}.") 

#Logical Operators
#Task 6
print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))    
bill = 0

if height >= 120:
    print("You can ride the rollercoaster")
    age = int(input("What is your age? "))
    if age < 12:
        bill = 5
        print("Please pay $5.")
    elif age < 18:
        bill = 7
        print("Please pay $7.")
    elif age >= 45 and age <= 55:
        bill = 0 #this is actually not needed. It will assume 0 if excluded
        print("Happy Mid-Life Crisis")
    else:
        bill = 12
        print("Please pay $12.")
    wants_photo = input("Do you want a photo taken? Type y for Yes or n for No.")
    if wants_photo == "y":
        bill += 3
    print(f"Your final bill is ${bill}")     
else:
    print("You CANNOT ride the rollercoaster")  

#Day 3 Project: Treasure Island (also Task 7)
print('''
                    ____...------------...____
               _.-"` /o/__ ____ __ __  __ \o\_`"-._
             .'     / /                    \ \     '.
             |=====/o/======================\o\=====|
             |____/_/________..____..________\_\____|
             /   _/ \_     <_o#\__/#o_>     _/ \_   \
             \_________\####/_________/
              |===\!/========================\!/===|
              |   |=|          .---.         |=|   |
              |===|o|=========/     \========|o|===|
              |   | |         \() ()/        | |   |
              |===|o|======{'-.) A (.-'}=====|o|===|
              | __/ \__     '-.\uuu/.-'    __/ \__ |
              |==== .'.'^'.'.====|
              |  _\o/   __  {.' __  '.} _   _\o/  _|
              `""""-""""""""""""""""""""""""""-""""`
''')
print("Welcome to Treasure Island!")
print("Your mission is to find the treasure.")

direction = input(
    "You're at a crossroads. Where do you want to go? Type left or right: "
).strip().lower()

if direction == "left":
    print("You reach a lake with an island in the middle.")
    choice = input("Type wait for a boat or swim across: ").strip().lower()

    if choice == "wait":
        print("The boat takes you safely to the island.")
        door = input("Choose a door: red, yellow, or blue: ").strip().lower()
        
        if door == "yellow":
            print("You found the treasure! You win!")
        elif door == "red":
            print("The room is full of fire. Game over.")
        elif door == "blue":
            print("You are eaten by beasts. Game over.")
        else:
            print("That door doesn't exist. Game over.")
    elif choice == "swim":
        print("A hungry trout attacks you. Game over.")
    else:
        print("You hesitate too long. Game over.")
else:
    print("You fall into a hole. Game over.")