from itertools import product


charset = "0123456789"
length = 4



for combination in product(charset, repeat=length):
    password = "".join(combination)
    print(password)


