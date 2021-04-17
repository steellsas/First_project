import time

def calc_time(func, arg):
    t1 = time.time()

    func(arg)

    runinig_time = time.time() - t1

    return runinig_time
lst = [1,5,6,8,4,25]
for i in lst:
    print(i)

