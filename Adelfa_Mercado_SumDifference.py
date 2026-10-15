#Arden Cristino S. Mercado II
#8-Adelfa
num1 = 0
num2 = 0
sum = 0
difference = 0

def get_number():
    global num1, num2
    num1 = int(input("Enter a number: "))
    num2 = int(input("Enter another number: "))

def calculate_sum():
    global sum
    sum = num1 + num2
    print(sum)

def calculate_difference():
    global difference
    difference = num1 - num2
    print(difference)

def display_sumDifference():
    calculate_sum()
    calculate_difference()

get_number()
calculate_sum()
calculate_difference()
display_sumDifference()

#why is sum broken?
