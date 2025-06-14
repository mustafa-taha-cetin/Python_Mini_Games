
print("The Love Calculator is calculating your score...")
name1 = input("What is your name? \n") # What is your name?
name2 = input("What is their name? \n") # What is their name?

name_together = name1 + name2
lower_names = name_together.lower()

t = lower_names.count("t")
r = lower_names.count("r")
u = lower_names.count("u")
e = lower_names.count("e")
first_digit = t + r + u + e

l = lower_names.count("l")
o = lower_names.count("o")
v = lower_names.count("v")
e = lower_names.count("e")
second_digit = l + o + v + e

score = int(str(first_digit) + str(second_digit))

if score < 10 or score > 90 and score < 100:
  print(f"Your score is {score}, you go together like coke and mentos.")
elif 40 <= score <= 50:
  print(f"Your score is {score}, you are alright together.")
elif score > 100:
  print(f"Your score is {score} ? you are %{score} compatible couple. Never hurt each other 'cause you'll never find a love like this.")
else:
  print(f"Your score is {score}.")


