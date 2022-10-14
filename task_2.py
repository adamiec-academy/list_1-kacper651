# CHESS BOARD
# pewnie da się lepiej przykminić albo rozdzielić te funkcje ale idk
def chess_board(n, k):
    for i in range(2 * n):
        if i % 2 == 0:
            print(n * ("  " + "##"))
            print(n * ("  " + "##"))
        else:
            print(n * ("##" + "  "))
            print(n * ("##" + "  "))


chess_board(4, 2)
