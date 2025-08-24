import math

def print_board(board):
    for i, row in enumerate(board): 
        print(f" {' | '.join(row)} ") 
        if i < len(board) - 1: 
            print("---+---+---")

def outcome(board):
    combos = (
        board,                                               
        [list(col) for col in zip(*board)],                  
        [[board[i][i] for i in range(3)]],                   
        [[board[i][2-i] for i in range(3)]]                  
    )
    for lines in combos:
        for line in lines:
            if all(cell == 'X' for cell in line):
                return 'X'
            elif all(cell == 'O' for cell in line):
                return 'O'
    if all(cell != ' ' for row in board for cell in row):
        return 'Draw'
    return None

def minimax_decision(board, maximizing):
    result = outcome(board)
    if result == 'X':
        return 1
    elif result == 'O':
        return -1
    elif result == 'Draw':
        return 0

    if maximizing:
        highest = -math.inf
        for r in range(3):
            for c in range(3):
                if board[r][c] == ' ':
                    board[r][c] = 'X'
                    eval_score = minimax_decision(board, False)
                    board[r][c] = ' '
                    highest = max(highest, eval_score)
        return highest
    else:
        lowest = math.inf
        for r in range(3):
            for c in range(3):
                if board[r][c] == ' ':
                    board[r][c] = 'O'
                    eval_score = minimax_decision(board, True)
                    board[r][c] = ' '
                    lowest = min(lowest, eval_score)
        return lowest

def select_best_move(board):
    best_val = -math.inf
    move = (-1,-1)
    for r in range(3):
        for c in range(3):
            if board[r][c] == ' ':
                board[r][c] = 'X'
                trial_val = minimax_decision(board, False)
                board[r][c] = ' '
                if trial_val > best_val:
                    best_val = trial_val
                    move = (r, c)
    return move

def tic_tac_toe():
    state = [[' ']*3 for _ in range(3)]
    print("You are 'O', the computer is 'X'. You go first.")
    while True:
        print_board(state)
        try:
            row = int(input("Choose your row (0, 1, 2): "))
            col = int(input("Choose your column (0, 1, 2): "))
        except ValueError:
            print("Please enter numerical values 0, 1, or 2.")
            continue
        if not (0 <= row <= 2 and 0 <= col <=2):
            print("Invalid cell. Pick 0, 1, or 2.")
            continue
        if state[row][col] != ' ':
            print("Cell already taken. Try another.")
            continue
        state[row][col] = 'O'
        final = outcome(state)
        if final:
            print_board(state)
            print("Game Over! Result:", final)
            break
        ai_row, ai_col = select_best_move(state)
        state[ai_row][ai_col] = 'X'
        final = outcome(state)
        if final:
            print_board(state)
            print("Game Over! Result:", final)
            break

if __name__ == "__main__":
    tic_tac_toe()
