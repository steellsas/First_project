
def is_corect(st):

    stack = []
    for j in st[::-1]:
        if j == ")":
            stack.append(j)
        if j == "(":
            stack.pop()
    if stack == []:
        print('True')
    else:
        print('False')

is_corect('')


# class stack():
#     def __init__(self,element):
#         self.elment = element
#
#     def push(self,lst):
#         self.lst.append
#     def pop():
#         pass
#
#     def s_len(self):
#         pass