# merge sotting
# lista daliname idu listus paskui dar i du kol gauname listus po viena elementa
# listas is vieno elemento jau yra surikiuotas.
# jungiame  i6dalintus listus po vinea

# def merge_sort(lst, sub_lst_L=[], sub_lst_r=[]):
#     l_lst = len(lst)
#
#     if l_lst > 1:
#
#         midle_of_lst = l_lst // 2
#
#         # get sub list
#         sub_lst_L = lst[:midle_of_lst]
#         sub_lst_r = lst[midle_of_lst:]
#
#         merge_sort(sub_lst_L)
#         merge_sort(sub_lst_r)
#         resul = []
#         i = i2 = n = 0
#
#         while i < len(sub_lst_L) and i2 < len(sub_lst_r):
#             if sub_lst_L[i] < sub_lst_r[i2]:
#                 lst[n] = sub_lst_L[i]
#                 i += 1
#             else:
#                 lst[n] = sub_lst_r[i2]
#                 i2 += 1
#             n += 1
#
#         while i < len(sub_lst_L):
#             lst[n] = sub_lst_L[i]
#             i += 1
#             n += 1
#
#         while i2 < len(sub_lst_r):
#             lst[n] = sub_lst_r[i2]
#             i2 += 1
#             n += 1
#
#         return lst


lst = [10, 2, 3, 41, 55, 6, 8, 65]
#print(merge_sort(lst))



def mergeSort(arr):
    if len(arr) == 1:
        print('>>>> base case:', arr, 'stopping recursion!')
        return arr
    mid = len(arr) // 2
    # print("len(arr) ", len(arr), arr)
    # print("middle ", mid)
    lft = arr[:mid]
    # print("left ", lft)
    rght = arr[mid:]
    # print("right ", rght)
    # print("="*100)
    res_left = mergeSort(lft)
    print('>>>> res_left:', res_left)
    res_right = mergeSort(rght)
    print('>>>> res_right:', res_right)
    print('[merging]', 'res_left:', res_left, 'res_right:', res_right)
    # merge dalis
    res_merged = []
    i_left = 0
    i_right = 0
    while i_left < len(res_left) and i_right < len(res_right):
        if res_left[i_left] <= res_right[i_right]:
            res_merged.append(res_left[i_left])
            i_left += 1
        else:
            res_merged.append(res_right[i_right])
            i_right += 1
    res_merged.extend(res_right[i_right:])
    res_merged.extend(res_left[i_left:])
    return res_merged
#lst = [38, 27, 43, 3, 9, 82, 10]
res = mergeSort(lst)
print('final:', res)