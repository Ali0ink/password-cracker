from itertools import product


def generate_passwords(charset, length):

    for combination in product(charset, repeat=length):
        yield "".join(combination)

