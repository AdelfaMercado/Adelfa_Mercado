#Arden Cristino S. Mercado II
#8-Adelfa
total_sales = 0
target_yes = 0
target_no = 0
food_items = int(input("Enter the amount of food you are buying"))
for i in range(food_items):
    sales = int(input(f"Enter the price for food {i + 1}: "))
    total_sales += sales
    if sales >= 500:
        target_yes += 1
    else:
        target_no += 1

def calculate_average():
    return total_sales / food_items
def display_report():
    print("="*50)
    print("CANTEEN SALES REPORT".center(50))
    print("=" * 50)
    print(f"The average sales is {calculate_average()} | Meeting target: {target_yes} | Did not meet target: {target_no}")

calculate_average()
display_report()
#i forgot how to do the digits