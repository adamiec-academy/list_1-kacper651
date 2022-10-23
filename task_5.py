def factorial(n):  # chyba najprostsze zadanie, ale może dlatego, że pisałem silnie 100 razy, nawet w asemblerze xd
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)


def report():
    for i in range(101):
        print(f"{i}! is {len(str(factorial(i)))} digits long")  # tego fstringa podpatrzyłem z zajęć sorry


report()
