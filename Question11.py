'''输入一个整数和进制，转换成十进制输出

输入格式:
在一行输入整数和进制
输出格式:
在一行十进制输出结果'''
a, n = input().split(",")
n = int(n)
flag = 0  # 记录当前要处理的是字符串a的第几位
sum = 0  # 转换为10进制后的结果
data = 1
# a:字符串
while flag < len(str(a)):
    currentData = int(a[len(a) - flag - 1])
    sum += data * (currentData)
    data = data * n
    flag += 1
print(sum)
