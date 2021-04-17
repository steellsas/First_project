# stingui
# listui
# dict

def ilgis(lst):
    s = 0
    for i in lst:
        s = s + 1
    print(s)


# len  functhion with re  for dict, list and string

def length_lst(lst, s1=0):
    if lst == []:
        return s1
    else:
        s1 = s1 + 1
        lst.pop(0)
        s1 = length_lst(lst, s1)
    return s1


#  function calculate deleted simbols of string.
def length_string(st, s_num=0):
    if st == "":
        return s_num
    else:
        s_num = s_num + 1
        return length_string(st[: -1], s_num)


def length_of_dict(dic, s_element=0):
    if dic == {}:
        return s_element
    else:
        s_element = s_element + 1
        # deleting firt key of
        dic.pop([*dic][0])
        s_element = length_of_dict(dic, s_element)
        return s_element


# test_list = [2, 4, 5, 4]
# print(f" List length {length_lst(test_list)}")

# sentence = "labas  16           "
# print(f" String - {sentence} - length  is {length_string(sentence)}")

# test_dict = {'Adomas': 12, '': 5, 'Rokas': 55, 'Andrius': 12, 'Romute': 25}
# print(f" dicthinary: {test_dict}  : length --->{length_of_dict(test_dict)} <-----")


def primary_number(num):
    num_lst = []
    p = 2
    for i in range(2, num + 1):
        num_lst.append(i)

    for

    print(num_lst)


primary_number(10)

# for n in num_lst:
# if (n % 2) == 0:
# mark number
#  num_lst[n] = -n
