# CHESS BOARD
def chess_board(n, k):
    for _ in range(n):
        for _ in range(k):
            print(n * (k * " " + k * "#"))
        for _ in range(k):
            print(n * (k * "#" + k * " "))


chess_board(4, 2)
