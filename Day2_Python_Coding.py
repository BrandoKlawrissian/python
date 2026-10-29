#Subscripting

#return first character
print("Hello"[0])

#return last character
print("Hello"[-1])

#Integer = Whole Number
print(123 + 345)

#Large Integers; underscores will add commas
print(123_456_789)

#Float = Floating Point Number
print(3.14159)

#Boolean
print(True)
print(False)

#this returns a type error
len(12345)

#change it to get rid of error
print("Hello")

#check data type or variable
print(type("Hello"))
# <class 'str'>

print(type(123))
# <class 'int'>

#Task 2
print(type("Hello"))
print(type(123))
print(type(123.456))
print(type(True))

#convert the string to integer
"123"
int("123")
print(int("123") + int("456"))

#Value Error is when you try to convert a data type that is not compatible; e.g. convert "ABC" to integer
int()
float()
str()
bool()

#Task 2 Pause 3
username = input("Enter your name")
length_of_username = len(username)
print("Number of letters in your name: " + str(length_of_username))

#Task 3 Pause 1
print(3 * 3 + 3 / 3 - 3) # equals 7
print(3 * (3 + 3) / 3 - 3) # equals 3

#Code Challenge BMI Calculator
weight = 84
height = 1.65
bmi = weight / height**2

print(bmi)

#Rounding
print(round(bmi)) #rounds to whole number

print(round(bmi, 2)) #rounds to two decimal places

#f string
score = 0
height = 1.8
is_winning = True

print(f"Your score is = {score}, your height is {height}. You are winning is {is_winning}.")

#Coding Challenge Tip Calculator
print("Welcome to the Tip Calculator!")
bill = float(input("What was the total bill? $"))
tip = int(input("How much tip would you like to give? 10, 12, or 15? "))
people = int(input("How many people to split the bill? "))

#Calculate Tip
tip_amount = bill * (tip/100)

#Calculate the total bill including the tip
total_bill = bill + tip_amount

#Split the bill
bill_per_person = round(total_bill / people, 2)
 
#Display the result
print(f"Each person should pay: ${bill_per_person}")