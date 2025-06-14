
#---------------------Logical Operators---------------------

print("---------------------------------------------")
print("Welcome to the rollercoaster")

boy = float(input("What is your height ? \n"))

if boy > 5:
    boy = boy
else:
    boy = boy * 100


if boy >= 120:
    print("You can ride bro ;))))")

    age = int(input("What's your age? \n"))

    if age < 12:
        print("You have to pay 5$, Have fun!")
    elif 18 >= age >= 12:
        print("You have to pay 7$, Have fun!")
    else:
        print("You have to pay 12$, Have fun! ")

else:
    print("You can't ride budy :((((")
