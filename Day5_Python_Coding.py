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

for number in range(1,101):
    if number % 3 == 0 and number % 5 == 0:
        print("FizzBuzz")
    elif number % 3 == 0:
        print("Fizz")
    elif number % 5 == 0:
        print("Buzz")
    else:
        print(number)