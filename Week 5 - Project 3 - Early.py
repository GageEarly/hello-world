import random
import math

smaller = int(input("Enter the smaller number: "))
larger = int(input("Enter the larger number: "))
maxAttempt = math.ceil(math.log2(larger - smaller + 1))

count = 0
while count != maxAttempt:
    count += 1
    guess = int((smaller + larger) / 2)
    print(smaller, larger)
    print("Your number is: ", guess)
    response = input("Enter =, <, or >: ")
    if response == '>':
        smaller = guess + 1
    elif response == '<':
        larger = guess - 1
    elif response == '=':
        print("Hooray, I've got it in", count, "tries!")
        break
    else:
        print("Invalid input. Please enter =, <, or >")
        count -= 1

if count >= maxAttempt and response != '=':
    print("I'm out of guesses, and you cheated")
