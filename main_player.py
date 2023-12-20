# Tic Tac Toe Program
print("Welcome to Tic Tac Toe")

from helpers import draw_board, check_turn, check_win, load_board_states, save_data
import json
import random

#TODO- be a little more descriptive with variable naming, ie. x= loadboardstates(), do board_states = ___

spots = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

playing = True
complete = False
turn = 0
last_turn = -1
move_number = 0
local_log_dict = {

}
winner = 'undefined'

player_choice = input("Player X starts the game. Enter X or O to indicate which player you want to be: ")
if player_choice not in ('X','O','x','o'):
    print("You did not enter a valid player choice. Please run the game again and enter a valid player choice")
    exit()
else:
    player_choice = player_choice.upper()
    if player_choice == 'X':
        leftover = 1
        AI_player = "O"
    else:
        leftover = 0
        AI_player = "X"
    print("\nThe game will now start. Pick a spot on the board by entering the corresponding number. Enter Q at any time to quit the game.\n")

board_states = load_board_states()
taken_spots = []
while playing: #Game loop
    move_number += 1
    draw_board(spots)

    print("__________\n")

    if move_number % 2 == leftover: #Human player turn
        while True:
            choice = input("[You] player " + player_choice + " which spot do you choose? ")
            if choice == 'Q':
                break
            elif choice not in [str(x) for x in range(1,10) ] or choice in taken_spots: #called a list comprehension
                print("Your input was invalid. Please enter a valid integer that is not already taken.")
                continue
            else:
                break
            taken_spots.append(str(choice))

    else: #AI turn
        random_play = random.choice(board_states[str(spots)]["options"])
        local_log_dict[str(spots)] = random_play
        choice = str(random_play)
        print("The AI player " + AI_player + " chose spot " + str(choice))
    taken_spots.append(str(choice))

    if choice in ['1','2','3','4','5','6','7','8','9']:
        choice = int(choice)
        row = (choice - 1) // 3
        column = (choice - 1) % 3
        if spots[row][column] not in ["X","O"]:
            turn += 1
            spots[row][column] = check_turn(turn)
    else:
        playing = False
        break

    if check_win(spots) == True:
        playing = False
        complete = True

    if turn > 8:
        playing = False

if complete == True:
    draw_board(spots)

    if check_turn(turn) == "X":
        print("\nPlayer X Wins!")
        winner = 'X'

    else:
        print("Player O Wins!")
        winner = 'O'

else:
    if choice == 'Q':
        print("\nYou exited the game.")
    else:
        draw_board(spots)
        print("\nThe game is tied. No winner.")
        print("Thanks for playing!")

