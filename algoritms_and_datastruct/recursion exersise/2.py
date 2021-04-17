from typing import List


def b_search_in_list(lst: List[int], k: int, start: int = 0, end: int = None):
    if end is None:
        end = len(lst) - 1

    if end >= start:
        mid = int(start + end) // 2

        if lst[mid] == k:
            return mid
        elif lst[mid] > k:
            return b_search_in_list(lst, k, start, mid - 1)
        else:
            return b_search_in_list(lst, k, mid + 1, end)


test_lst = [4, 6, 7, 8, 10, 40]
x = 40
print('indeksas', b_search_in_list(test_lst, x))

