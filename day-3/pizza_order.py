print("Welcome to Python Pizza Deliveries!")

size = input("What size pizza do you want? S, M or L: ")
pepperoni = input("Do you want pepperoni on your pizza? Y or N: ")
extra_cheese = input("Do you want extra cheese? Y or N: ")

small_pizza = 15
medium_pizza = 20
large_pizza = 25
total_bill = 0
if size == 'S':
    total_bill += small_pizza
    if pepperoni == 'Y':
        total_bill += 2
    if extra_cheese == 'Y':
        total_bill += 1

elif size == "M":
    total_bill += medium_pizza
    if pepperoni == 'Y':
        total_bill += 3
    if extra_cheese == 'Y':
        total_bill += 1

else:
    total_bill += large_pizza
    if pepperoni == 'Y':
        total_bill += 3
    if extra_cheese == 'Y':
        total_bill += 1

print(f"Your final bill is: ${total_bill}")
