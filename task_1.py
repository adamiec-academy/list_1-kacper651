#CROSS

def cross(n):                               #rysowanie krzyża z "kwadratów "o boku 4
    for i in range(n):
        print(n * " " + n * "*" + n * " ")
    for i in range(n):
        print(3 * n * "*")
    for i in range(n):
        print(n * " " + n * "*" + n * " ")


cross(4)

