def checkNumber(board, check_board, number):
    for value in board:
        if int(board[value]) == int(number):
            check_board[value] = True
    return check_board

def checkWin(check_boards):
    for num, check_board in enumerate (check_boards):
        # rows
        for r in range (0,5):
            if check_board[r,0] and check_board[r,1] and check_board[r,2] and check_board[r,3] and check_board[r,4]:
                return num, check_board
        # columns
        for c in range (0,5):
            if check_board[0,c] and check_board[1,c] and check_board[2,c] and check_board[3,c] and check_board[4,c]:
                return num, check_board
    return None, None

def checkAllWin(check_boards, winners):
    for num, check_board in enumerate (check_boards):
        # rows
        for r in range (0,5):
            if check_board[r,0] and check_board[r,1] and check_board[r,2] and check_board[r,3] and check_board[r,4] and num not in winners:
                winners.append(num)
        # columns
        for c in range (0,5):
            if check_board[0,c] and check_board[1,c] and check_board[2,c] and check_board[3,c] and check_board[4,c] and num not in winners:
                winners.append(num)
    return winners

if __name__ == "__main__":
    data = open("input.dat").read().splitlines()
    random_numbers = [int(number) for number in data[0].split(",")]

    boards = [] ; check_boards = []
    new_board = {} ; new_check_board = {}
    row = 0
    for line in data[2:]:
        if line == "":
            row = 0
            boards.append(new_board)
            check_boards.append(new_check_board)
            new_check_board = {} ; new_board = {}
        else:
            for col, number in enumerate (line.split()):
                new_board[row, col] = number
                new_check_board[row, col] = False
            row += 1

    for number in random_numbers:
        for board, check_board in zip (boards, check_boards):
            check_board = checkNumber(board, check_board, number)
        number_board_win, winner_board = checkWin(check_boards)
        if winner_board is not None:
            break
    summation = 0
    for found, value in zip (check_boards[number_board_win].values(),boards[number_board_win].values()):
        if not found:
            summation += int(value)
    print("Sum of all unmarked numbers multiplied by the number that was just called:", number*summation)

    boards = [] ; check_boards = []
    new_board = {} ; new_check_board = {}
    row = 0
    for line in data[2:]:
        if line == "":
            row = 0
            boards.append(new_board)
            check_boards.append(new_check_board)
            new_check_board = {} ; new_board = {}
        else:
            for col, number in enumerate (line.split()):
                new_board[row, col] = number
                new_check_board[row, col] = False
            row += 1
    winners = []
    for number in random_numbers:
        for board, check_board in zip (boards, check_boards):
            check_board = checkNumber(board, check_board, number)
        winners = checkAllWin(check_boards, winners)
        if len(winners) == len(boards):
            break
    summation = 0
    for found, value in zip (check_boards[winners[-1]].values(),boards[winners[-1]].values()):
        if not found:
            summation += int(value)
    print("Sum of all unmarked numbers multiplied by the number that was just called:", number*summation)