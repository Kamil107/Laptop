import math

def QuadraticRoots(a, b, c):
    delta = b ** 2 - 4 * a * c
    if delta == 0:
        x = -b / 2 * a
        print(f"Jest jedno rozwiązanie: {x=}")
    elif delta > 0:
        x1 = (-b + math.sqrt(delta)) / 2 * a
        x2 = (-b - math.sqrt(delta)) / 2 * a
        print(f"Są dwa rozwiązania: {x1=} i {x2=}")
    else:
        print(f"Nie ma rozwiązań, {delta=}")


QuadraticRoots(1, 4, 5)