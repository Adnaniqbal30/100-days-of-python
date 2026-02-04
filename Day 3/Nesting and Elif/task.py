print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))

if height >= 120:
    print("You can ride the rollercoaster")
    age=int(input("Enter Your Age"))
    if age<=18:
        print("Please Pay $5")
    else:
        print("Please Pay $10")
else:
    print("Sorry you have to grow taller before you can ride.")
