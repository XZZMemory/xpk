'''给定两个均不超过9的正整数a和n，要求编写程序求a+aa+aaa++⋯+aa⋯a（n个a）之和。'''
a, n = input().split()
a, n = int(a), int(n)
data = a
sum = 0
while n > 0:
    sum += data
    data = data * 10 + a
    n = n - 1
print("s = " + str(sum))
