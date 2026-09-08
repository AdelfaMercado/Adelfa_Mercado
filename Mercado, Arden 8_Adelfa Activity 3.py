import math
#Project title
#Hypotenuse Calculator Activity

#input stage
print("Enter side a and b to calculate the hypotenuse")
SideA = float(input("enter side a: "))
SideB = float(input("enter side b: "))

#Processing
ASquared = math.pow(SideA, 2)
BSquared = math.pow(SideB, 2)

#I forgot about C and I don't want to rename the variables
CSquared = ASquared + BSquared

hypotenuse = math.sqrt(CSquared)
print(f"the hypotenuse is:{hypotenuse:.2f}")


