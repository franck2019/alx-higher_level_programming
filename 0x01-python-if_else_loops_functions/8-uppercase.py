#!/usr/bin/python3

def uppercase(str):

    """
    uppercase - function that returns uppercase of a string

    params:
        - str, a string

    return:
        - The string str in uppercase

    Description:
        since ord('a') = 97 and ord('z') = 122 and
    ord('A') = 65 and ord('Z') = 90, we remark that the dif-
    ference between upper and lower characters is 32. We just
    need to use the char function to retrieve the uppercase e-
    quivalent.
    """
    res = ""

    for i in range(len(str)):

        if ord(str[i]) >= 97 and ord(str[i]) <= 122:
            c = ord(str[i]) - 32
            c = chr(c)
        else:
            c = str[i]

        res += c

    print("{}".format(res))
