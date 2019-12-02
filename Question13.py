'''输入2个正整数lower和upper（lower≤upper≤100），请输出一张取值范围为[lower，upper]、且每次增加2华氏度的华氏-摄氏温度转换表。
温度转换的计算公式：C=5×(F−32)/9，其中：C表示摄氏温度，F表示华氏温度。
输入格式:
在一行中输入2个整数，分别表示lower和upper的值，中间用空格分开。
输出格式:
第一行输出："fahr celsius"
接着每行输出一个华氏温度fahr（整型）与一个摄氏温度celsius（占据6个字符宽度，靠右对齐，保留1位小数）。
若输入的范围不合法，则输出"Invalid."。
'''
lower, upper = input().split()
lower, upper = int(lower), int(upper)
if lower > upper or upper > 100 or lower < 0:
    print("Invalid.")
    exit(0)
print("{:6}".format("fahr"), "{:6}".format("celsius"))
for i in range(lower, upper + 1, 2):
    data_str = str(5 * (i - 32) / 9).partition(".")
    print(data_str[0] + data_str[1] + data_str[2][0])
    print("{:6}".format(str(i)), data_str[0] + data_str[1] + data_str[2][0], end="")
    print("  " + str(5 * (i - 32) / 9))
