import json

def draw_board(spots):
    board = (f"|{spots[0][0]}|{spots[0][1]}|{spots[0][2]}|\n"
             f"|{spots[1][0]}|{spots[1][1]}|{spots[1][2]}|\n"
             f"|{spots[2][0]}|{spots[2][1]}|{spots[2][2]}|")
    print(board)

def check_turn(turn):
    if turn % 2 == 0:
        return "O"
    else:
        return "X"

def load_board_states():
   with open('data.json', 'r') as file:
       board_states = json.load(file)
       return board_states

def save_data(data):
    with open('data.json', 'w') as file:
        json.dump(data, file, indent=4)

def check_win(spots):
    if (spots[0][0] == spots[0][1] == spots[0][2]
            or spots[1][0] == spots[1][1] == spots[1][2]
            or spots[2][0] == spots[2][1] == spots[2][2]
            or spots[0][0] == spots[1][0] == spots[2][0]
            or spots[0][1] == spots[1][1] == spots[2][1]
            or spots[0][2] == spots[1][2] == spots[2][2]
            or spots[2][0] == spots[1][1] == spots[0][2]
            or spots[0][0] == spots[1][1] == spots[2][2]):
        return True

    else:
        return False
