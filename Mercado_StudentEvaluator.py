#Arden Cristino S. Mercado II
#8-Adelfa
#setting a variable


#Functions
def display_header():
    print("-"*50)
    print("Student Evaluator".center(50))
    print("-" *50)

display_header()
#Global variables
student_name = input("Please enter your name: ")
assessment1 = int(input("Please enter your assessment: "))
assessment2 = int(input("Please enter your assessment: "))
assessment3 =int(input("Please enter your assessment: "))


display_header()

def get_student_info():
    print(f"Student Name: {student_name}")
    print(f"Assessment 1: {assessment1}")
    print(f"Assessment 2: {assessment2}")
    print(f"Assessment 3: {assessment3}")

def evaluate_performance():
    average_score= (assessment1 + assessment2 + assessment3)/3
    if 89 <= average_score <= 100:
        print("Outstanding my good sir")

    elif 84 <= average_score <= 89:
        print("Very Satisfactory sir")

    elif 79 <= average_score <= 84:
        print("Just Satisfactory")

    elif 74 <= average_score <= 79:
        print("Fairly Satisfactory")

    elif 0 <= average_score <= 74:
        print("You need some improvement you absolute twat I have seen babies with more score than you out of a true and false test and they got it 10 times")

def display_report():
    get_student_info()
    display_header()
    evaluate_performance()
    display_header()

display_report()