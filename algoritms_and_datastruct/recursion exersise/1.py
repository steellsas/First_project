def b_search_in_list(lst, k):
    start = 0
    end = len(lst) - 1
    while start <= end:
        mid = int(start + end) // 2

        if lst[mid] == k:
            return mid
        elif lst[mid] < k:
            start = mid + 1
        else:
            end = mid - 1


test_lst = [4, 6, 7, 8, 10, 40]
x = 10
print('indeksas', b_search_in_list(test_lst, x))
