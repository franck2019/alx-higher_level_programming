#!/usr/bin/python3


def list_division(my_list_1, my_list_2, list_length):

    ml1 = my_list_1
    ml2 = my_list_2
    ll = list_length

    result_list = []
    for i in range(list_length):

        result = 0

        try:
            result = ml1[i] / ml2[i]
        except TypeError:
            print("wrong type")
        except ZeroDivisionError:
            print("division by 0")
        except IndexError:
            print("out of range")
        finally:
            result_list.append(result)

    return result_list
