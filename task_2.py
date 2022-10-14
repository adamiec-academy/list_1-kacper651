# CHESS BOARD
# pewnie da się lepiej przykminić albo rozdzielić te funkcje ale idk
def chess_board(n, k):
    for i in range(n):
        print(n * (k * " " + k * "#"))
        print(n * (k * " " + k * "#"))
        print(n * (k * "#" + k * " "))
        print(n * (k * "#" + k * " "))


chess_board(4, 2)
