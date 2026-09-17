import re #For pattern validation
#Name: Arden Cristino S. Mercado II
#8-Adelfa
#9/17/26

#Payment method checker
Valid_Payment_Method = ["Cash","GCash" , "Card"]

Payment_Method = input("Please enter your payment method:").lower()

if Payment_Method in Valid_Payment_Method:
    print("Payment Method is valid",Payment_Method.capitalize())
else:
    print("Invalid Payment Method")
    print("Please try again")
print(" ")
print("===================================================================")
print(" ")
#Grade Checker
grade = int(input("Please enter your grade:"))

if 0 <= grade <= 100:
    print("Grade is valid",grade)
else:
    print("Invalid Grade")
    print(" ")
    print("===================================================================")
    print(" ")
#Student ID Checker
student_id = input("Please enter your student id: ")

pattern = r"\d{4}-\d{4}"

if re.fullmatch(pattern, student_id):
    print("Student ID is valid",student_id)
else:
    print("Invalid Student ID")
    print(" ")
    print("===================================================================")
    print(" ")
#PIN Validator
pin = input("Please enter your 4 Digit PIN (Specifically 4 digits do not mess this up: ")

if len(pin) == 4 and pin.isdigit():
    print("PIN is valid",pin)
else:
    print("Invalid PIN (I told you so)")
    print(" ")
    print("===================================================================")
    print(" ")
#Student Score Entry
exam_score = int(input("Please enter your examination score: "))

if 0 <= exam_score <= 100 and ValueError:
    print("Examination score is valid",exam_score)
else:
    print("Invalid Examination Score (nice try)")
    print(" ")
    print("===================================================================")
    print(" ")