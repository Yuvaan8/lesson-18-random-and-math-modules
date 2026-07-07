import random
playing = True
number = str(random.randint(0,9))
while playing:
    guess = input('Guess a number between 0 - 9:')
    if guess == number:
        print('nice guess! You guessed it!')
        print('the number was', number)
        break
    else:
        print('wrong guess try again!', number)