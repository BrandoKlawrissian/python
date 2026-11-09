# fruits = ["Apple", "Peach", "Pear"]
# for fruit in fruits:
#     print(fruit)
#     print(fruit + " pie")

# student_scores = [150, 142, 185, 120, 171, 184, 149, 24, 59, 68, 199, 78, 65, 89, 86, 55, 91, 64, 89]
# print(range(1, 10))

# student_scores = [180, 124, 165, 173, 189, 169, 146]
# total_score = sum(student_scores)
# print("Total score:", total_score)
#
# student_scores = [180, 124, 165]
#
# sum = 0
# for score in student_scores:
#     sum += score
#
# print(sum)

# student_scores = [8, 65, 89, 86, 55, 91, 64, 89]
# highest_score = student_scores[0]
# for score in student_scores:
#     if score > highest_score:
#         highest_score = score
# print(highest_score)

# sum = 0
# for number in range(0, 101):
#     sum += number
# print(sum)

# for number in range(1,101):
#     if number % 3 == 0 and number % 5 == 0:
#         print("FizzBuzz")
#     elif number % 3 == 0:
#         print("Fizz")
#     elif number % 5 == 0:
#         print("Buzz")
#     else:
#         print(number)

import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

password = []

for letter in range(nr_letters):
    random_letter = random.choice(letters)
    password.append(random_letter)
for symbol in range(nr_symbols):
    random_symbol = random.choice(symbols)
    password.append(random_symbol)
for number in range(nr_numbers):
    random_number = random.choice(numbers)
    password.append(random_number)

random.shuffle(password)

final_password = ""
for character in password:
    final_password += character

print("Your final password is: " + final_password)
