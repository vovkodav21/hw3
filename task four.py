import random
gueesses_taken = 0
number_random = random.randint(1, 10)
input_name = input("What is your name?: ")
number_str = str(number_random)
print("So, " + input_name + "," + " Lets play the game! I will generate a random number and your task is to guess it. You have 3 tries!")
for guesses_taken in range(3):
    print('try to guess.')
    guess = input()
    guess = int(guess)
    if guess < number_random:
        print("Your number is too low")
    if guess > number_random:
        print("Your number is too big")
    if guess == number_random:
        break
if guess == number_random:
    guesses_taken = str(guesses_taken + 1)
    print('Perfect, ' + input_name + '! You won with' + guesses_taken + ' guesses!')
if guess != number_random:
    print('Oops. You loose. I generated the number ' + number_str)
