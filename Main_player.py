# Tic Tac Toe Program
print("Welcome to Tic Tac Toe")

from Helpers import draw_board, check_turn, check_win, load_board_states, save_data
import json
import random

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
    print("You did not enter a valid player choice. Please run the game again, and enter a valid player choice")
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

while playing: #explain here
    move_number += 1
    draw_board(spots)
    #Add this board state to local log

    print("__________\n")
    if last_turn == turn:
        print("That spot is taken, pick an open spot")
    last_turn = turn

    if move_number % 2 == leftover: # Human player turn
        choice = input("[You] player " + player_choice + " which spot do you choose? ")

    else: #AI turn
        x = load_board_states()
        random_play = random.choice(x[str(spots)]["options"])
        local_log_dict[str(spots)] = random_play
        choice = str(random_play)
        print("The AI player " + AI_player + " chose spot " + str(choice))


    if choice == 'Q':
        playing = False
    elif choice in ['1','2','3','4','5','6','7','8','9']:
        choice = int(choice)
        row = (choice - 1) // 3
        column = (choice - 1) % 3
        if spots[row][column] not in ["X","O"]:
            turn += 1
            spots[row][column] = check_turn(turn)
    #TODO: Finish this, if choice not in ['1','2','3','4','5','6','7','8','9']:



    if check_win(spots) == True:
        playing = False
        complete = True

    if turn > 8:
        playing = False

draw_board(spots)

if complete == True:
    if check_turn(turn) == "X":
        print("Player X Wins!")
        winner = 'X'


    else:
        print("Player O Wins!")
        winner = 'O'

else:
    print("The game is tied. No winner.")
    print("Thanks for playing!")

print(local_log_dict) # DELETE once you confirm this is right, doesn't need to be on the output

#Updating the JSON file depending on if X or O wins

if winner == 'X':
    x_gameStates = {}
    index = 0
    for state, move in local_log_dict.items():
        if index % 2 == 0:
            x_gameStates[state] = move
        index += 1
    # x = load_board_states()     #CHECK does this make sense? Before you run it and start changing the JSON file
    # for state,move in x_gameStates.items():
    #     x[state]["options"].append(move)
    # save_data(x)

    print(x_gameStates) # DELETE once you confirm this is right, doesn't need to be on the output

elif winner == 'O':
    o_gameStates = {}
    index = 0
    for state, move in local_log_dict.items():
        if index % 2 == 1:
            o_gameStates[state] = move
        index += 1
    # x = load_board_states()      #CHECK does this make sense? Before you run it and start changing the JSON file
    # for state, move in o_gameStates.items():
    #     x[state]["options"].append(move)
    # save_data(x)
    print(o_gameStates) # DELETE once you confirm this is right, doesn't need to be on the output

else:
    winner = 'none'

