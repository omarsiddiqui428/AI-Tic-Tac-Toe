# Tic Tac Toe Program
print("Welcome to Tic Tac Toe")

from helpers import draw_board, check_turn, check_win, load_board_states, save_data
import json
import random

def play_game():
    global total_games, total_x, total_o, total_draws #TODO: Ask why i needed to declare them here as well
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
    local_log_dict = {} #local log to keep track of board states
    winner = 'undefined'
    board_states = load_board_states()

    while playing: #Game loop
        move_number += 1
        draw_board(spots)

        print("__________\n")
        if last_turn == turn:
            print("That spot is taken, pick an open spot")
        last_turn = turn

        random_play = random.choice(board_states[str(spots)]["options"])
        local_log_dict[str(spots)] = random_play

        choice = str(random_play)
        if choice == 'Q':
            playing = False
        elif choice in ['1','2','3','4','5','6','7','8','9']:
            choice = int(choice)
            row = (choice - 1) // 3
            column = (choice - 1) % 3
            if spots[row][column] not in ["X","O"]:
                turn += 1
                spots[row][column] = check_turn(turn)

        if check_win(spots) == True:
            playing = False
            complete = True

        if turn > 8:
            playing = False

    draw_board(spots)

    if complete == True:
        if check_turn(turn) == "X":
            print("Player 1 Wins!")
            winner = 'X'

        else:
            print("Player 2 Wins!")
            winner = 'O'

    else:
        print("The game is tied. No winner.")
        print("Thanks for playing!")

    print(local_log_dict) #Printing for records and validation purposes

    #Updating the JSON file depending on if X or O wins

    if winner == 'X':
        x_gameStates = {} #Local log to just store the board states for where X moves, relevant when X wins
        index = 0
        for state, move in local_log_dict.items():
            if index % 2 == 0:
                x_gameStates[state] = move
            index += 1

        # Updating the winning moves in the JSON file if X wins
        board_states["AI Training Summary"]["Total X-Won games"] += 1
        for state,move in x_gameStates.items():
            board_states[state]["options"].append(move)
        save_data(board_states)

        print(x_gameStates) #Printing for records and validation purposes

    elif winner == 'O':
        o_gameStates = {} #Local log to just store the board states for where O moves, relevant when O wins
        index = 0
        for state, move in local_log_dict.items():
            if index % 2 == 1:
                o_gameStates[state] = move
            index += 1

        # Updating the winning moves in the JSON file if O wins
        board_states["AI Training Summary"]["Total O-Won games"] += 1
        for state, move in o_gameStates.items():
            board_states[state]["options"].append(move)
        save_data(board_states)
        print(o_gameStates)

    else:
        #Will train the AI based on draws as well since the ideal AI would either win or draw a game. Tic Tac Toe is almost impossible to win every time since there are so few options to make
        winner = 'none'
        board_states["AI Training Summary"]["Total draws"] += 1
        for state, move in local_log_dict.items(): #will add all the board states and moves for when the game results in a draw
            board_states[state]["options"].append(move)
        save_data(board_states)
        print(local_log_dict)

    board_states = load_board_states()
    board_states["AI Training Summary"]["Total games"] += 1
    save_data(board_states)

    return winner

#Loop to train the AI against its self below
games_to_play = 200

for g in range(games_to_play):
    result = play_game()






