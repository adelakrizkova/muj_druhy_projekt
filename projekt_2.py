'''
projekt_2.py: druhý projekt do Engeto Online Python Akademie
author: Adéla Křížková
email: adela.krizkova@karlinblok.cz
discord: Adule
'''

import random

print("Hi there!", "-" * 60,
      "I´ve generated a random 4 digit number for you.",
      "Let´s play a bulls and cows game.", "-" * 60, sep="\n")

random_num = "0000"
while random_num[0] == "0":
      digit_list = list(range(0, 10))
      random_num_list = random.sample(digit_list, 4)
      random_num = str(random_num_list)[1:11:3]

guesses = 0
while True:
    number = input("Enter a number: ")
    if len(number) != 4 or not number.isdigit() or number[0] == "0" or len(set(number)) != 4:
        print("The number must have 4 digits, every digit must be unique and can´t start with 0.")
        continue

    bulls = 0
    cows = 0

    for i in range(4):
        if random_num[i] == number[i]:
            bulls += 1
        elif random_num[i] in number:
            cows += 1

    guesses += 1
    if random_num == number:
        break

    if bulls == 1:
        print(bulls, "bull")
    else:
        print(bulls, "bulls")

    if cows == 1:
        print(cows, "cow")
    else:
        print(cows, "cows")

print("Correct, you´ve guessed the right number in", guesses, "guesses.")
print(60 * "-")
if guesses <= 5:
      print("That´s amazing.")
elif guesses > 5 and guesses <= 10:
      print("That´s average.")
else:
      print("That´s not so good.")