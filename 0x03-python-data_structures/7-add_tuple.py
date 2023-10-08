#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):

    # Addition of tuples
    # using map() + lambda
    res = tuple(map(lambda i, j: i + j, tuple_a, tuple_b))
    for e in tuple_a
    return res

tuple_a = (1, 89)
tuple_b = (88, 11)
new_tuple = add_tuple(tuple_a, tuple_b)
print(new_tuple)

print(add_tuple(tuple_a, (1, )))
print(add_tuple(tuple_a, ()))
