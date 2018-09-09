from random import randint


print('-------------------------------------------------')
print('             GUESS THE NUMBER APP')
print('-------------------------------------------------')
print()

number = randint(1, 100)
guess = None

while guess != number:
    guess = int(input('Guess a number between 1 and 100: '))
    if guess > number:
        print('Sorry but {} is HIGHER than the number\n'.format(guess))
    elif guess < number:
        print('Sorry but {} is LOWER than the number\n'.format(guess))
    else:
        print("YES! You've got it. The number was {}".format(number))
