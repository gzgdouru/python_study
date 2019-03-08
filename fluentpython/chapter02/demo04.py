'''
列表的坑
'''

if __name__ == "__main__":
    board = [["_"] * 3 for i in range(3)]
    print(board)
    board[1][2] = "X"
    print(board)

    print("-"*80)

    weird_board = [["_"] * 3] * 3
    print(weird_board)
    weird_board[1][2] = "X"
    print(weird_board)