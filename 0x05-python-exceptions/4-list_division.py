#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    new_list = []
    if list_length <= 0:
        print("out of range")
        return new_list
    for i in range(list_length):
        try:
            elem = my_list_1[i]/my_list_2[i]
        except ZeroDivisionError:
            elem = 0
            print("division by 0")
        except TypeError:
            elem = 0
            print("wrong type")
        except IndexError:
            elem = 0
            print("out of range")
        finally:
            new_list.append(elem)
    return new_list
