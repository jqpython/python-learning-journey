def play_game(board_size):
    board = []
    for _ in range(board_size):
        row = ["."] * board_size
        board.append(row)

    player = "X"
    groups_to_check = generate_groups_to_check(board_size)

    while not is_game_over(board, groups_to_check):
        print(print_board(board))
        print("It's " + player + "'s turn.")
        # Get valid move from player
        while True:
            try:
                row = int(input("Enter a row (0-{}): ".format(board_size - 1)))
                column = int(input("Enter a column (0-{}): ".format(board_size-1)))

                # Check if row and column are within bounds
                if row < 0 or row >=board_size or column < 0 or column >= board_size:
                    print("Row and column must be within the board dimensions.")
                    continue

                # Check if the cell is empty
                if board[row][column] != ".":
                    print("That cell is already occupied. Choose another. ")
                    continue

                break

            except ValueError:
                print("Please enter valid integers for row and column.")
            except IndexError:
                print("Row and coulumn must be within the board dimensions.")

        board = make_move(board, row, column, player)

        # Switch player
        if player == "X":
            player = "O"
        else:
            player = "X"

    print(print_board(board))
    # Check if there is a winner
    winner_found = False
    for group in groups_to_check:
        if is_group_complete(board,group) and are_all_cells_the_same(board, group):
            winner_found = True
            break

    if is_board_full(board) and not winner_found:
        print("Game over! it's a draw")
    else:
        winner = "O" if player == "X" else "X"
        print("Gamer over! Player " + winner + " wins!")

def is_board_full(board):
    for row in board:
        if "." in row:
            return False
    return True

def print_board(board):
    formatted_rows = []
    for row in board:
        formatted_rows.append(" ".join(row))
    grid = "\n".join(formatted_rows)
    return grid

def make_move(board,row, column, player):
    board[row][column] = player
    return board

def generate_groups_to_check(n):
    groups = [] # [[(0,0), (0,1), (0,2)], [(1,0),(1,1),(1,2)], [(2,0),(2,1),(2,2)]

    # add rows
    for row in range(n): # 0
        group = []
        for col in range(n): # 0
            group.append((row,col))
        groups.append(group)

    # add columns
    for col in range(n):
        group = []
        for row in range(n):
            group.append((row,col))
        groups.append(group)

    diagonal1 = []
    for i in range(n):
        diagonal1.append((i,i))
    groups.append(diagonal1)

    diagonal2 = []
    for i in range(n):
        diagonal2.append((i, n-1-i))
    groups.append(diagonal2)

    return groups

def get_cells(board, coords):
    return [board[coord[0]][coord[1]] for coord in coords]

def is_group_complete(board, coords):
    cells = get_cells(board, coords)
    return "." not in cells

def are_all_cells_the_same(board, coords):
    cells = get_cells(board, coords)
    if len(cells) == 0:
        return False
    first = cells[0]
    if first == ".":
        return False
    return all(cell == first for cell in cells)

def is_game_over(board, groups_to_check):
    for group in groups_to_check:
        if is_group_complete(board,group):
            if are_all_cells_the_same(board, group):
                return True
    if is_board_full(board):
        return True

    return False

def main():
    board_size = 3
    print("Board Size: {} x {}".format(board_size, board_size))
    play_game(board_size)

if __name__ == "__main__":
    main()
