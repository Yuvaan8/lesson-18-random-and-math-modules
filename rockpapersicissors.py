import random
playing = True
while True:
    user_choice = input('Enter your choice:')
    possible_choices = ['rock', 'paper', 'scissors']
    computer_choice = random.choice(possible_choices)
    if user_choice == computer_choice:
       print('Its a tie')
    elif user_choice == 'rock':
        if computer_choice == 'scissors':
          print('you win! rock crushes scissors')
        else:
          print('you lose! paper covers rock')
    elif user_choice == 'paper':
        if computer_choice == 'rock':
          print('You win! paper covers rock')
        else:
           print('you lose! scissors cuts paper')
    elif user_choice == 'scissors':
        if computer_choice == 'paper':
           print('you win! scissors cuts paper')
        else:
           print('you lose! rock crushes scissors')
    play_again = input('Do you want to play again? (yes/no):')
    if play_again != 'yes':
       break

    
          

