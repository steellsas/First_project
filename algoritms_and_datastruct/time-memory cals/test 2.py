"""
1. + Odd or Even number,
2. + Look-up table (dict)
3. + Find all possible pizza combinations [desra, suris, grybai, jalapenai, majonezas, silke, burokas, ...] -> len(lst) = n
4. + Find all permutations of a given set/string
5. + Finding element on sorted list with binary search
6. + Find max element in unsorted list
7. + 3 variables equation solver  4x + 8y + 10z = n, kur n duodamas, kaip parametras
8. + Find duplicate elements in list **(naïve)**
9. + Find duplicate elements in list using dict
10. Sorting elements in list with merge sort  ***
11. Sorting array with bubble sort  ***
"""
import itertools
from itertools import chain, combinations

[1]
[1, 2]
[2, 1]
[1, 2, 3]
[2, 1, 3]
[2, 3, 1]
[3, 2, 1]
[3, 1, 2]
[1, 3, 2]


def max_in_unsorted_list_6(lst):
    max_value = lst[0]
    for n in lst:
        if n > max_value:
            max_value = n
    return max_value


# unsorted_list = [6, 4, 12, 8, 1, 3, 3, 15, 2]
# print(max_in_unsorted_list_6(unsorted_list))
def pizza_cmb_3(lst):
    cmb = []
    if not isinstance(lst, list):
        return cmb
    if len(lst) == 0:
        return cmb
    if len(lst) == 1:
        return lst
    if len(lst) >= 2:
        for elem in lst:
            cmb.append(elem)
            for elem2 in lst:
                if elem != elem2 and lst.index(elem) < lst.index(elem2):
                    cmb.append(elem + ' ' + elem2)
        return cmb


# toppings = ['a', 'b', 'c', 'd']
# print(pizza_cmb_3(toppings))
def check_for_duplicates_8(lst):
    seen = []
    for i in lst:
        if i in seen:
            print("duplicate", i)
            return i
        else:
            seen.append(i)


def check_for_duplicates_9(lst):
    seen = {}
    for i in lst:
        if i in seen:
            print("duplicate", i)
            return i
        else:
            seen[i] = 1


lst = [1, 2, 3, 1, 2]
print(check_for_duplicates_8(lst))
print(check_for_duplicates_9(lst))


# a_list = [1, 2, 1]
# contains_duplicates = any(a_list.count(element) > 1 for element in a_list)
# print(contains_duplicates)
def find_element_with_binary_search5(lst, elm):
    k = 0
    d = len(lst) - 1
    while k <= d:
        vid = k + (d - k) // 2;
        if lst[vid] == elm:
            return vid
        elif lst[vid] < elm:
            k = vid + 1
        else:
            d = vid - 1


# lst = list(range(10, 1000000, 1))
#
# print(find_element_with_binary_search5(lst, 128))
def eq_solver_7(n):
    result = []
    for x in range(1, 101):
        for y in range(1, 101):
            for z in range(1, 101):
                if 4 * x + 8 * y + 10 * z == n:
                    # print(f'x={x}; y={y}; z={z}')
                    result.append([x, y, z])
    return result


# n = 58
# print(eq_solver_7(n))
def look_up_table_dict_2(lst, elm):
    # list_to_dict = dict.fromkeys(lst, elm)
    list_to_dict = {i: lst[i] for i in range(0, len(lst))}
    res = list_to_dict[elm]
    return res
    # print(f"ieškomas elementas {elm}")
    # print(list_to_dict)
    # for key, value in list_to_dict.items():
    #     if value == elm:
    #         print(f"ieškomo elemento {elm} raktas yra {key}")


# lst = list(range(10, 20, 1))
# print(look_up_table_dict_2(lst, 5))
"""
[1,2,3]
[2,1,3]
[2,3,1]
[3,2,1]
[3,1,2]
[1,3,2]
"""
# def permutation(lst):
#     # If lst is empty then there are no permutations
#     if len(lst) == 0:
#         return []
#
#         # If there is only one element in lst then, only
#     # one permuatation is possible
#     if len(lst) == 1:
#         return [lst]
#
#     # Find the permutations for lst if there are
#     # more than 1 characters
#
#     l = []  # empty list that will store current permutation
#
#     # Iterate the input(lst) and calculate the permutation
#     for i in range(len(lst)):
#         m = lst[i]
#
#         # Extract lst[i] or m from the list.  remLst is
#         # remaining list
#         remLst = lst[:i] + lst[i + 1:]
#
#         # Generating all permutations where m is first
#         # element
#         for p in permutation(remLst):
#             l.append([m] + p)
#     return l
# # Driver program to test above function
# data = list('123')
# for p in permutation(data):
#     print
#     p
lst = [1, 2, 3]


def permutation_4(lst):
    result = []
    per = itertools.permutations(lst)
    for val in per:
        # print(*val)
        result.append(list(val))
    return result


def pizza_topings_3(lst):
    s = list(lst)
    res = chain.from_iterable(combinations(s, r) for r in range(len(s) + 1))
    return list(res)


print(pizza_topings_3(lst))
# print(permutation_4(lst))
