'''读入2个正整数A和B，1<=A<=9, 1<=B<=10,产生数字AA...A,一共B个A

输入格式:
在一行中输入A和B。

输出格式:
在一行中输出整数AA...A,一共B个A'''
a, b = input().split(",")
b = int(b)
a = str(int(a))
str1 = ""
while b > 0:
    str1 += a
    b = b - 1
print(str1)
