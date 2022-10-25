# ENVELOPE

def envelope(n):
    print((2 * n + 1) * "*")  # PODSTAWA GÓRNA

    for i in range(n - 1):
        print("*" + i * " " + "*" + (2 * (n - i) - 3) * " " + "*" + i * " " + "*")  # CIAŁO 1, nwm jak ale chyba działa hihi

    print("*" + (n - 1) * " " + "*" + (n - 1) * " " + "*")  # ŚRODEK

    for i in range(n - 2, -1, -1):
        print("*" + i * " " + "*" + (2 * (n - i) - 3) * " " + "*" + i * " " + "*")

    print((2 * n + 1) * "*")  # PODSTAWA DOLNA


envelope(4)
