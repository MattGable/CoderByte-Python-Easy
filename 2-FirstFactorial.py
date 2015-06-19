# for num, return num*num-1*num-2etc...or, for 5, return (5*4*3*2*1), etc.


def first_factorial(num):
    z = 1
    for i in range(num):
        j = i + 1
        z = z * j
    return z

print first_factorial(7)
