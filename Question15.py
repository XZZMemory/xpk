'''本题要求编写程序，根据输入的三角形的三条边a、b、c，计算并输出面积和周长。注意：在一个三角形中， 任意两边之和大于第三边。三角形面积计算公式：area=√
​s(s−a)(s−b)(s−c),其中s=(a+b+c)/2。
输入格式：
输入为3个正整数，分别代表三角形的3条边a、b、c。
输出格式：
如果输入的边能构成一个三角形，则在一行内，按照area = 面积; perimeter = 周长
的格式输出，保留两位小数。否则，输出These sides do not correspond to a valid triangle'''
a, b, c = input().split()
a, b, c = int(a), int(b), int(c)
if a + b <= c or a + c <= b or b + c <= a:
    print("These sides do not correspond to a valid triangle")
    exit(1)
s = (a + b + c) / 2
area = (s * (s - a) * (s - b) * (s - c))**0.5
print("area = {:.2f}; perimeter = {:.2f}".format(area, s * 2))
