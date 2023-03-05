import random
num = random.randint(1,20)
count = 0
print('I am thinking of a number between 1 and 20.')
while True:
    print('Take a guess.')
    guess = input()
    if int(guess) < num:
        print('Your guess is too low.')
        count = count + 1
    elif int(guess) > num:
        print('Your guess is too high.')
        count = count + 1
    else:
        count = count + 1
        print('Good job! You guessed my number in ' + str(count) + ' guesses!')
        break