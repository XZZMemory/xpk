'''输入格式:
输入在一行中给出某用户的月用电量（单位：千瓦时）。

输出格式:
在一行中输出该用户应支付的电费（元），结果保留两位小数，格式如：“cost = 应付电费值”；若用电量小于0，则输出"Invalid Value!"。'''
n = float(input())
cost = 0
if n < 0:
    print("Invalid Value!")
    exit(0)
elif n <= 50:
    cost = n * 0.53
else:
    cost = n * 0.53 + (n - 50) * 0.05
print("cost = {:.2f}".format(cost))
