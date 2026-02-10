try:
    age = int(input("How old are you?"))
except ValueError:
    print("Please write only integer")
    age = int(input("How old are you?"))
if age > 18:
    print(f"You can drive at age {age}.")
