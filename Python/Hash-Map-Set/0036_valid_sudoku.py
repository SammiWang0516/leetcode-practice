# 36 valid sudoku
'''
Determine if a 9 x 9 Sudoku board is valid. Only the filled cells need to be validated according to the following rules:
Each row must contain the digits 1-9 without repetition.
Each column must contain the digits 1-9 without repetition.
Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without repetition.
Note:
A Sudoku board (partially filled) could be valid but is not necessarily solvable.
Only the filled cells need to be validated according to the mentioned rules.

Example 1:
Input: board =
[["5","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]
Output: true

Example 2:
Input: board =
[["8","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]
Output: false
Explanation: Same as Example 1, except with the 5 in the top left corner being modified to 8. Since there are two 8's in the top left 3x3 sub-box, it is invalid.
'''
'''
def isValidSudoku(board):
    # each input number shall check 3 times, one is the same row, one is the same column, and the last one is to check the 3x3 square
    # slice the list of list so that it check row duplicate first; original input list makes perfect input
    square = [{} for _ in range(9)]
    for i in range(9):                          # control row index
        row = {}
        column = {}
        for j in range(9):                      # control column index
            if board[i][j] != '.':              # ignore the empty slot
                # check each row
                if board[i][j] not in row:
                    row[board[i][j]] = 1
                else:
                    return False
                # check for square (row count to prevent repeatly count)
                if i < 3:
                    if j < 3:
                        if board[i][j] not in square[0]:
                            square[0][board[i][j]] = 1
                        else:
                            return False
                    elif 3 <= j < 6:
                        if board[i][j] not in square[1]:
                            square[1][board[i][j]] = 1
                        else:
                            return False
                    else:
                        if board[i][j] not in square[2]:
                            square[2][board[i][j]] = 1
                        else:
                            return False
                elif 3 <= i < 6:
                    if j < 3:
                        if board[i][j] not in square[3]:
                            square[3][board[i][j]] = 1
                        else:
                            return False
                    elif 3 <= j < 6:
                        if board[i][j] not in square[4]:
                            square[4][board[i][j]] = 1
                        else:
                            return False
                    else:
                        if board[i][j] not in square[5]:
                            square[5][board[i][j]] = 1
                        else:
                            return False
                else:
                    if j < 3:
                        if board[i][j] not in square[6]:
                            square[6][board[i][j]] = 1
                        else:
                            return False
                    elif 3 <= j < 6:
                        if board[i][j] not in square[7]:
                            square[7][board[i][j]] = 1
                        else:
                            return False
                    else:
                        if board[i][j] not in square[8]:
                            square[8][board[i][j]] = 1
                        else:
                            return False
            if board[j][i] != '.':              # ignore the empty slot
                # check each column
                if board[j][i] not in column:
                    column[board[j][i]] = 1
                else:
                    return False
    return True
'''
def isValidSudoku(board):
    from collections import defaultdict
    # three things need to check, row-check, column-check, and square-check
    # for checking, we use default dictionary with the value being set()
    row = defaultdict(set)
    column = defaultdict(set)
    square = defaultdict(set)
    for i in range(9):              # i control row number
        for j in range(9):          # j control column number
            if board[i][j] != '.':
                if board[i][j] in row[i] or board[i][j] in column[j] or board[i][j] in square[(i // 3, j // 3)]:
                    return False
                row[i].add(board[i][j])
                column[j].add(board[i][j])
                square[(i // 3, j // 3)].add(board[i][j])
    return True

board = [["5","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]
print(isValidSudoku(board))