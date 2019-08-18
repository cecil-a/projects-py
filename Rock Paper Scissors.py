player_name_1 = input('Player 1 what is your name: \n')

player_name_2 = input('Player 2 what is your name: \n')

while True:

    player_1 = input((player_name_1) + ', please choose Rock, Paper or Scissors (rock/paper/scissors): ')

    player_2 = input((player_name_2) + ', please choose Rock, Paper or Scissors (rock/paper/scissors): ')

    if player_1 == 'rock' and player_2 == 'scissors' or player_1 == 'paper' and player_2 == 'rock' or player_1 == 'scissors' and player_2 == 'paper':

        print(player_name_1 + ' wins!')

    elif player_2 == 'rock' and player_1 == 'scissors' or player_2 == 'paper' and player_1 == 'rock' or player_2 == 'scissors' and player_1 == 'paper':

        print(player_name_2 + ' wins!')

    elif player_2 == 'rock' and player_1 == 'rock' or player_2 == 'paper' and player_1 == 'paper' or player_2 == 'scissors' and player_1 == 'scissors':

        print('That was a draw')

    else:

        print('Error! Invalid input. Please type paper for Paper, scissors for Scissors or rock for Rock')

    if input('Do you want to start a new game? Type yes or no (y/n): \n') == 'n':

        break