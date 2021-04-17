import random

lst = [9, 9, 9, 9, 9, 9, 1]
# lst =[ random.randint(1,20) for i in range(20)]

count = 0
pas_count = 0
c = 0
for i in range(len(lst)):
    for j in range(len(lst) - 1):
        if lst[j + 1] < lst[j]:
            lst[j], lst[j + 1] = lst[j + 1], lst[j]
            count += 1
    c += 1
pas_count += 1
print(lst)
print(count, pas_count, c)

######--------- gedo

import random

#
lst = [random.randint(0, 10) for i in range(random.randint(1, 50))]

print(lst)
swap = True
while swap:
    swap = False
    for i in range(0, len(lst) - 1):
        if lst[i] > lst[i + 1]:
            lst[i + 1], lst[i] = lst[i], lst[i + 1]
            swap = True


##---------------- greitestnis

def bubbleSort(arr):
    n = len(arr)

    # Traverse through all array elements
    for i in range(n):

        # Last i elements are already in place
        for j in range(0, n - i - 1):

            # traverse the array from 0 to n-i-1
            # Swap if the element found is greater
            # than the next element
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

# Driver code to test above
