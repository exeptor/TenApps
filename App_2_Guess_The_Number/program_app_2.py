import random

print('-------------------------------------')
print('        GUESS THE NUMBER')
print('-------------------------------------')
print()

random_number = random.randint(0, 100)
your_name = input('What is your name? ')
guess = -1
first_guess = ''    # used this way in its first appearance only; on the second it will be changed

while guess != random_number:
    raw_guess = input('What is your{} guess {}? '.format(first_guess, your_name))
    guess = int(raw_guess)
    first_guess = ' next'   # change on the second appearance in the loop to enrich user experience

    if guess < random_number:
        print('Sorry {}, {} is LOWER!'.format(your_name, guess))
    elif guess > random_number:
        print('Sorry {}, {} is HIGHER!'.format(your_name, guess))
    else:
        print('Congratulation {}, {} is the correct number!'.format(your_name, guess))
