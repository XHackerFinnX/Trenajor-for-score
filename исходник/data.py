import random


def proverka():
    global s
    return s


def deistvit_1(x, y):
    global deis, s
    if deis == '+':
        s = x + y
    elif deis == '-':
        s = x - y
    elif deis == '*':
        s = x * y
    elif deis == '/':
        s = x // y
    return x, deis, y, '='


def score(x):
    global deis
    while True:
        if x == 1:
            one = random.randint(0, 10)
            two = random.randint(0, 10)
            deis_1 = ['+', '-', '*', '/']
            deis = random.choice(deis_1)
            if deis == '+':
                return deistvit_1(one, two)
            elif deis == '-':
                if one - two >= 0:
                    return deistvit_1(one, two)
                else:
                    continue
            elif deis == '*':
                one = random.randint(1, 10)
                two = random.randint(0, 10)
                return deistvit_1(one, two)
            elif deis == '/':
                one = random.randint(1, 100)
                two = random.randint(1, 10)
                if one % two == 0:
                    return deistvit_1(one, two)
                else:
                    continue
        elif x == 2:
            one = random.randint(0, 100)
            two = random.randint(0, 100)
            deis_1 = ['+', '-', '*', '/']
            deis = random.choice(deis_1)
            if deis == '+':
                return deistvit_1(one, two)
            elif deis == '-':
                if one - two >= 0:
                    return deistvit_1(one, two)
                else:
                    continue
            elif deis == '*':
                one = random.randint(1, 100)
                two = random.randint(0, 10)
                return deistvit_1(one, two)
            elif deis == '/':
                one = random.randint(1, 1000)
                two = random.randint(1, 10)
                if one % two == 0:
                    return deistvit_1(one, two)
                else:
                    continue
        elif x == 3:
            one = random.randint(0, 1000)
            two = random.randint(0, 1000)
            deis_1 = ['+', '-', '*', '/']
            deis = random.choice(deis_1)
            if deis == '+':
                return deistvit_1(one, two)
            elif deis == '-':
                if one - two >= 0:
                    return deistvit_1(one, two)
                else:
                    continue
            elif deis == '*':
                one = random.randint(1, 1000)
                two = random.randint(0, 10)
                return deistvit_1(one, two)
            elif deis == '/':
                one = random.randint(1, 1000)
                two = random.randint(1, 100)
                if one % two == 0:
                    return deistvit_1(one, two)
                else:
                    continue
        elif x == 4:
            one = random.randint(0, 10000)
            two = random.randint(0, 10000)
            deis_1 = ['+', '-', '*', '/']
            deis = random.choice(deis_1)
            if deis == '+':
                return deistvit_1(one, two)
            elif deis == '-':
                if one - two >= 0:
                    return deistvit_1(one, two)
                else:
                    continue
            elif deis == '*':
                one = random.randint(1, 1000)
                two = random.randint(0, 100)
                return deistvit_1(one, two)
            elif deis == '/':
                one = random.randint(1, 10000)
                two = random.randint(1, 100)
                if one % two == 0:
                    return deistvit_1(one, two)
                else:
                    continue
