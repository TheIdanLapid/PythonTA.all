def power_new(a,b):
    """ computes a**b using iterated squaring """
    count = 0
    result = 1
    b_bin = bin(b)[2:]
    reverse_b_bin = b_bin[: :-1]
    for bit in reverse_b_bin:
        if bit == '1':
            result = result * a
            count+=1
        a = a * a
        count+=1
    print(count)
    return result

def power(a,b):
    result=1
    count = 0
    while b>0: # b is nonzero
        if b % 2 == 1: # b is odd
            result = result*a # )פעולת כפל אחת(
            count+=1
        a = a*a # )פעולת כפל אחת(
        count+=1
        b = b//2
    print(count)
    return result

power(2,15)
