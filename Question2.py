'''在同一行依次输入三个值a,b,c，用空格分开，输出 b*b-4*a*c的值

输入格式:
在一行中输入三个数。

输出格式:
在一行中输出公式值。'''
a, b, c = input().split()
a, b, c = int(a), int(b), int(c)
d = b * b - 4 * a * c
print(d)
