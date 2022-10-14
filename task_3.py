# ENVELOPE (wersja alfa, bo wzór się psuje i nwm czy ma działac tylko dla "4" czy da się to uogólnić XD)
import math


def envelope(n):
    print((2 * n + 1) * "*")  # PODSTAWA GÓRNA

    for i in range(n - 1):
        print("*" + i * " " + "*" + (math.ceil((2 * n + 1) / 2) - 2 * i) * " " + "*" + i * " " + "*")  # CIAŁO 1

    print("*" + math.floor((2 * n + 1) / 3) * " " + "*" + math.floor((2 * n + 1) / 3) * " " + "*")  # ŚRODEK

    for i in range(n - 2, 0, -1):
        print("*" + i * " " + "*" + (math.ceil((2 * n + 1) / 2) - 2 * i) * " " + "*" + i * " " + "*")  # CIAŁO 2

    print((2 * n + 1) * "*")  # PODSTAWA DOLNA


envelope(4)
