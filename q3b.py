def binary_calculation(s):
    binary_num = ""
    while s > 0:
        if s%2 == 1 :
            binary_num += "1"
        else:
            binary_num += "0"
        s = s//2
    return binary_num[::-1]

def making_number(n):
    number = 0
    length = len(n)
    for i in range(length):
        bit = int(n[length - 1 - i])
        number += bit * (2 ** i)
    return number


def add_binary(a, b):
    if a.startswith("0b"):
        a = a[2:]
    if b.startswith("0b"):
        b = b[2:]
    p = making_number(a) + making_number(b)
    
    return "0b" + binary_calculation(p)