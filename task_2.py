# CHESS BOARD
# pewnie da się lepiej przykminić albo rozdzielić te funkcje ale idk
def chess_board(n, k):
    for i in range(2 * n):
        if i % 2 == 0:
            print(n * (2 * "  " + 2 * "##"))
            print(n * (2 * "  " + 2 * "##"))
        else:
            print(n * (2 * "##" + 2 * "  "))
            print(n * (2 * "##" + 2 * "  "))


chess_board(4, 2)
