#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    n = min(len(my_list_1), len(my_list_2))
    diff = 0
    if list_length > n:
        diff = list_length - n
        print("out of range")
    new_list = []
    for i in range(n):
        try:
            elem = my_list_1[i]/my_list_2[i]
        except ZeroDivisionError:
            elem = 0
            print("division by 0")
        except TypeError:
            elem = 0
            print("wrong type")
        finally:
            new_list.append(elem)
    for i in range(diff):
        new_list.append(0)
    return new_list
