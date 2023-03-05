import random
num = random.randint(1,20)
count = 0
print('I am thinking of a number between 1 and 20.')
for i in range(6):
    print('Take a guess.')
    guess = int(input())
    if guess < num:
        print('Your guess is too low.')
        count = count + 1
    elif guess > num:
        print('Your guess is too high.')
        count = count + 1
    else:
        count = count + 1
        break
if guess == num:
    print('Good job! You guessed my number in ' + str(count) + ' guesses!')
else:
    print('Nope. The number I was thinking of was ' + str(num))