import math

'''a = 5
print("                a = ",a,"地址为：",id(a))
a += 1
print("a+=1后         ","a = ",a,"地址为：",id(a))
b = 5
print("                b = ",b,"地址为：",id(b))
c = b
print("                c = ",c,"地址为：",id(c))'''
print(type(1J))
print(type(1 / 2))
print(type(1 // 2))
a = 121 + 1.21
print(type(a))
print("******************")
print(0xA + 0xB)
print(type(1 + 2 * 3.14 > 0))
print(math.sqrt(4) * math.sqrt(9))
print(chr(65))
print(10 + 5 // 3 - True + False)
print(3 ** 2 ** 3)
print(round(17.0 / 3 ** 2, 2))
print(0 and 1 or not 2 < True)
print(pow(-3, 2), round(18.67, 1), round(18.67, -1))
print(round(123.84, 0), round(123.84, -2), math.floor(15.5))
print(int("20", 16), int("101", 2))
print("*************")
print(hex(16), bin(10))
a = 3
b = 5
c = 6
d = True
print(not d or a >= 0 and a + c > b + 3)
print(abs(-10.2), round(abs(8 - 2j), 3))
print("&&&&&&&&&&")
x = True
y = False
z = False
print(x or y and z)
x = 0
y = True
print(x >= y and 'A' < 'B')
print("&&&&&&&&&&")
print(16 - 25 > 78 / 2 or "XYZ" != "xyz" and not (10 - 6 > 18 / 2))
print("hello" 'world')
print(((2 >= 2) or (2 < 2)) and 2)
print(3 and 0 and 5)
x=3
x='3'
print(x)
a = int(input())
n = int(input())
print(sum([int('a' * i) for i in range(1, n + 1)]))