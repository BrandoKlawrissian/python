# import random
# import my_module

# random_integer = random.randint(1, 10)
# print(random_integer)

# print(my_module.my_favorite_number)

# random_number_0_to_1 = random.random()
# print(random_number_0_to_1)

# random_number_0_to_1 = random.random() *10
# print(random_number_0_to_1)

# random_float = random.uniform(1, 10)
# print(random_float)
#Task 1
# coin_toss = random.randint(0,1)
# if coin_toss == 0:
#     # print(coin_toss)
#     print("Heads")
# else:
#     # print(coin_toss)
#     print("Tails")

# #Task 2
# fruits = ["Cherry", "Apple", "Pear"]
# states_of_america = [
#     "Delaware",
#     "Pennsylvania",
#     "New Jersey",
#     "Georgia",
#     "Connecticut",
#     "Massachusetts",
#     "Maryland",
#     "South Carolina",
#     "New Hampshire",
#     "Virginia",
#     "New York",
#     "North Carolina",
#     "Rhode Island",
#     "Vermont",
#     "Kentucky",
#     "Tennessee",
#     "Ohio",
#     "Louisiana",
#     "Indiana",
#     "Mississippi",
#     "Illinois",
#     "Alabama",
#     "Maine",
#     "Missouri",
#     "Arkansas",
#     "Michigan",
#     "Florida",
#     "Texas",
#     "Iowa",
#     "Wisconsin",
#     "California",
#     "Minnesota",
#     "Oregon",
#     "Kansas",
#     "West Virginia",
#     "Nevada",
#     "Nebraska",
#     "Colorado",
#     "North Dakota",
#     "South Dakota",
#     "Montana",
#     "Washington",
#     "Idaho",
#     "Wyoming",
#     "Utah",
#     "Oklahoma",
#     "New Mexico",
#     "Arizona",
#     "Alaska",
#     "Hawaii",
# ]

# print(states_of_america[0])

# #Task 2
# fruits = ["Cherry", "Apple", "Pear"]
# fruits[-1] #this will be "Pear"

# fruits = ["Cherry", "Apple", "Pear"]
# fruits[0] = "Orange"
# # fruits will now become ["Orange", "Apple", "Pear"]

# fruits = ["Cherry", "Apple", "Pear"]
# fruits.append("Orange")
# fruits will now become ["Cherry", "Apple", "Pear", "Orange"]

#Task 3
# import random
# friends = ["Alice", "Bob", "Charlie", "David", "Emanuel"]

# print(random.choice(friends))

# random_index = random.randint(0,len(friends)-1)
# random_name = friends[random_index]
# print(random_name)

# states_of_america = ["Delaware", "Pennsylvania", "New Jersey", "Georgia", "Connecticut", "Massachusetts", "Maryland",
#                      "South Carolina", "New Hampshire", "Virginia", "New York", "North Carolina", "Rhode Island",
#                      "Vermont", "Kentucky", "Tennessee", "Ohio", "Louisiana", "Indiana", "Mississippi", "Illinois",
#                      "Alabama", "Maine", "Missouri", "Arkansas", "Michigan", "Florida", "Texas", "Iowa", "Wisconsin",
#                      "California", "Minnesota", "Oregon", "Kansas", "West Virginia", "Nevada", "Nebraska", "Colorado",
#                      "North Dakota", "South Dakota", "Montana", "Washington", "Idaho", "Wyoming", "Utah", "Oklahoma",
#                      "New Mexico", "Arizona", "Alaska", "Hawaii"]

# print(states_of_america)

# fruits = ["Cherry", "Apple", "Pear"]
# print(fruits[3]) #This will be an IndexError

# fruits = ["Cherry", "Apple", "Pear"]
# veg = ["Cucumber", "Kale", "Spinnach"]
# fruits_and_veg = [fruits, veg]
#The list would look like this: [["Cherry", "Apple", "Pear"], ["Cucumber", "Kale", "Spinnach"]]

# ["Cherry", "Apple", "Pear"]
# ["Cucumber", "Kale", "Spinnach"]

import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''


choices = ["Rock", "Paper", "Scissors"]
choices_ascii = [rock, paper, scissors]
player_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper, 2 for Scissors\n"))
computer_choice = random.randint(0,2)
print("You chose: ", choices[player_choice], "\n", choices_ascii[player_choice])
print("Computer chose: ", choices[computer_choice], "\n", choices_ascii[computer_choice])

if player_choice == computer_choice:
    print("It's a tie!")
elif player_choice == 0 and computer_choice == 2:
    print("You win!")
elif player_choice == 1 and computer_choice == 0:
    print("You win!")
elif player_choice == 2 and computer_choice == 1:
    print("You win!")
else:
    print("Computer wins!")

##############################################################################
import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

game_images = [rock, paper, scissors]

user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
# Note: it's worth checking if the user has made a valid choice before the next line of code.
# If the user typed somthing other than 0, 1 or 2 the next line will give you an error.
# You could for example write:
if user_choice >= 0 and user_choice <= 2:
    print(game_images[user_choice])

computer_choice = random.randint(0, 2)
print("Computer chose:")
print(game_images[computer_choice])

if user_choice >= 3 or user_choice < 0:
    print("You typed an invalid number. You lose!")
elif user_choice == 0 and computer_choice == 2:
    print("You win!")
elif computer_choice == 0 and user_choice == 2:
    print("You lose!")
elif computer_choice > user_choice:
    print("You lose!")
elif user_choice > computer_choice:
    print("You win!")
elif computer_choice == user_choice:
    print("It's a draw!")