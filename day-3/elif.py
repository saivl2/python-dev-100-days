print("Welcome to the rollercoaster!")

height = int(input("What is your height in cm? "))
age = int(input("Enter age: "))
bill = 0
if height >= 120:
    print('You can ride the rollercoaster')
    if age <= 12:
        bill += 5
        print(f'Pay ${bill}')
    elif age <= 18:
        bill += 7
        print(f'Pay ${bill}')
    else:
        bill += 12
        print(f'Pay ${bill}')
    wants_photo = input("Do you want a photo taken? ")

    if wants_photo == 'yes':
        # Add $3
        bill += 3
        print(f"Pay ${bill}")
    else:
        print(f"Pay ${bill}")


else:
    print('SOrry you have to grow taller before you write')