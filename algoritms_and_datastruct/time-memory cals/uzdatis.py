"""
1. Odd or Even number,
2. Look-up table (dict)

def look_up_table_dict2(lst, elm):
    # list_to_dict = dict.fromkeys(lst, elm)
    list_to_dict = {i: lst[i] for i in range(0, len(lst))}
    print(f"ieškomas elementas {elm}")
    print(list_to_dict)
    for key, value in list_to_dict.items():
        if value == elm:
            print(f"ieškomo elemento {elm} raktas yra {key}")


lst = list(range(10, 20, 1))

look_up_table_dict2(lst, 19)
3. Find all possible pizza combinations

lst = [1, 2, 3, 4]
result = []
for val in lst:
    result.append([val])
print('Initial configuration:', result)
for i in range(len(lst)-1):
    print(f'ITERATION: {i}')
    config_count = 0
    old_config_numb = len(result)
    while config_count < old_config_numb:
        old_config = result.pop(0)
        # print('old_config', old_config)
        available_values = list(set(lst).difference(set(old_config)))
        for val in available_values:
            new = old_config + [val]
            # extend configuration
            result.append(new)
        print(f'[config_count={config_count}]; {result}')
        config_count += 1
    # print(result)
    print('='*100)
print(len(result))

4. Find all permutations of a given set/string

toppings = ['desra', 'grybai', 'jelapenai', 'suris']
result = []
if len(toppings) >= 1:
    result.append([0])
    result.append([1])
    print('Initial configuration:', result)
# raise Exception
for i in range(len(toppings)-1):
    print(f'ITERATION: {i}')
    config_count = 0
    old_config_numb = len(result)
    print('old_config_numb:', old_config_numb)
    while config_count < old_config_numb:
        old_config = result.pop(0)
        # print('old_config', old_config)
        new0 = old_config + [0]
        new1 = old_config + [1]
        # extend configuration
        result.append(new0)
        result.append(new1)
        print(f'[config_count={config_count}]; {result}')
        config_count += 1
    print(result)
    print('='*100)
print(len(result))
topping_configs = []
for config in result:
    topping_config = [toppings[i] for i, flag in enumerate(config) if flag == 1]
    topping_config = ', '.join(topping_config)
    topping_configs.append(topping_config)
print(topping_configs)

5. Finding element on sorted list with binary search

def max_in_unsorted_list():
    unsorted_list = [6, 4, 12, 8, 1, 3, 3, 15, 2]
    max_value = unsorted_list.pop(0)
    for n in unsorted_list:
        if n > max_value:
            max_value = n
    return max_value

6. Find max element in unsorted list"""

def max_in_unsorted_list():
    unsorted_list = [6, 4, 12, 8, 1, 3, 3, 15, 2]
    max_value = unsorted_list.pop(0)
    for n in unsorted_list:
        if n > max_value:
            max_value = n
    return max_value

"""
7. 3 variables equation solver
padariau pirmą dalį lst = [22, 44]

for n in lst:

        for x in range(1, 101):
            for y in range(1, 101):
                for z in range (1, 101):
                    if 4*x + 8*y + 10*z == n:
                        print(x)
                        print(y)
                        print(z)
                        
8. Duplicate elements in list **(naïve)**
9. Duplicate elements in list using dict
"""


# 1

#  3
import math
def posible(lst):
    l = len(lst)
    ll =[]
    posible_len = math.factorial(l)
    for item in range(l):
        m = lst[item]
        d = lst[:item] + lst[item + 1:]
        for i in range(len(d)):

            ll.append([m] + [d[i]])
        print(ll)

       # new_lst = lst[:item] + lst[item + 1:]

       # for item in new_lst:
        #print(new_lst)


posible([1,2,3])


lst1 = [1, 2, 3]
lst2 = [1, 2, 3]

if lst1 == lst2 :
    print('taip')
else:
    print("ne")


# Python function to print permutations of a given list
def permutation(lst):
    # If lst is empty then there are no permutations
    if len(lst) == 0:
        return []

        # If there is only one element in lst then, only
    # one permuatation is possible
    if len(lst) == 1:
        return [lst]

        # Find the permutations for lst if there are
    # more than 1 characters

    l = []  # empty list that will store current permutation

    # Iterate the input(lst) and calculate the permutation
    for i in range(len(lst)):
        m = lst[i]
        remLst = lst[:i] + lst[i + 1:]

        # Generating all permutations where m is first
        # element
        for p in permutation(remLst):
            l.append([m] + p)
    return l

# Driver program to test above function

#for p in permutation([1,2,3,4,5]):
  #  print(p)
