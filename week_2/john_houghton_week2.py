def to_number(str):
    str = int(str)
    return str

def add_two(n1, n2):
    the_sum = n1 + n2
    return the_sum

def cube(n):
    cubed = n**3
    return cubed

print(cube(add_two(to_number('2'), to_number('4'))))