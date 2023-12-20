# Tic Tac Toe Program
print("Welcome to Tic Tac Toe")

from Helpers import draw_board, check_turn, check_win, load_board_states, save_data
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
    local_log_dict = {}
    winner = 'undefined'

    while playing: #explain here
        move_number += 1
        draw_board(spots)

        print("__________\n")
        if last_turn == turn:
            print("That spot is taken, pick an open spot")
        last_turn = turn

        x = load_board_states()
        random_play = random.choice(x[str(spots)]["options"])
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

    print(local_log_dict) # TODO: DELETE once you confirm this is right, doesn't need to be on the output

    #Updating the JSON file depending on if X or O wins

    if winner == 'X':
        x_gameStates = {}
        index = 0
        for state, move in local_log_dict.items():
            if index % 2 == 0:
                x_gameStates[state] = move
            index += 1
        # Updating the winning moves in the JSON file if X wins
        x = load_board_states()
        x["AI Training Summary"]["Total X-Won games"] += 1
        for state,move in x_gameStates.items():
            x[state]["options"].append(move)
        save_data(x)

        print(x_gameStates) # TODO: DELETE once you confirm this is right, doesn't need to be on the output

    elif winner == 'O':
        o_gameStates = {}
        index = 0
        for state, move in local_log_dict.items():
            if index % 2 == 1:
                o_gameStates[state] = move
            index += 1
        # Updating the winning moves in the JSON file if O wins
        x = load_board_states()
        x["AI Training Summary"]["Total O-Won games"] += 1
        for state, move in o_gameStates.items():
            x[state]["options"].append(move)
        save_data(x)
        print(o_gameStates) # TODO: DELETE once you confirm this is right, doesn't need to be on the output

    else:
        winner = 'none'
        x = load_board_states()
        x["AI Training Summary"]["Total draws"] += 1
        save_data(x)

    x = load_board_states()
    x["AI Training Summary"]["Total games"] += 1
    save_data(x)

    return winner


games_to_play = 1000

for g in range(games_to_play):
    result = play_game()







