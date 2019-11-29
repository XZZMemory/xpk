'''本题要求将输入的任意3个整数从小到大输出。

输入格式:
输入在一行中给出3个整数，其间以空格分隔。

输出格式:
在一行中将3个整数从小到大输出，其间以“->”相连。'''
a, b, c = input().split()
a, b, c = int(a), int(b), int(c)
# 小的赋值给变量a，大的赋值给变量b
if a > b:
    temp = a
    a = b
    b = temp
if c < a:
    print(str(c) + "->" + str(a) + "->" + str(b))
else:  # c<a
    if c < b:
        print(str(a) + "->" + str(c) + "->" + str(b))
    else:
        print(str(a) + "->" + str(b) + "->" + str(c))
