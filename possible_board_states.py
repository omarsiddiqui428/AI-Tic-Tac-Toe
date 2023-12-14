from pprint import pprint
import json

def generate_tic_tac_toe_combinations():
    # Initialize an empty board
    board = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]

    # Dictionary to store all unique board states
    all_combinations = {}

    # Recursive function to generate board combinations
    def generate_combinations(current_board, next_player, available_positions):
        # Convert the board to a string to use as a dictionary key
        board_str = str(current_board)

        # If this board state has not been seen before, add it to the dictionary
        if board_str not in all_combinations:
            all_combinations[board_str] = {
                "options": available_positions.copy()
            }

            # Iterate over each available position
            for pos in available_positions:
                new_board = [row.copy() for row in current_board]
                new_board[(pos - 1) // 3][(pos - 1) % 3] = next_player
                new_available_positions = available_positions.copy()
                new_available_positions.remove(pos)

                # Recursive call with the updated board and the next player
                generate_combinations(new_board, 'O' if next_player == 'X' else 'X', new_available_positions)

    # Start the recursion with the initial board
    generate_combinations(board, 'X', list(range(1, 10)))

    return all_combinations

# Generate the combinations
tic_tac_toe_combinations = generate_tic_tac_toe_combinations()

# Output the full dictionary (note: this will be a large output)
pprint(tic_tac_toe_combinations)

with open('data.json', 'w') as file:
    json.dump(tic_tac_toe_combinations, file, indent=4)