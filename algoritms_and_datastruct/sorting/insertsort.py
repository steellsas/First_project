import random
lst =[4, 9, 10, 3, 9, 3, 1, 2, 9]
#lst =[ random.randint(1,20) for i in range(20)]

for i in range(len(lst)):
    for j in range(len(lst[0:i+1])):
        if lst[i] < lst[j]:
            lst[j], lst[i] = lst[i], lst[j]

print(lst)
