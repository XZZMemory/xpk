a, b = input().split()
a, b = int(a), int(b)
sum = 0
flag = 1
while a <= b:
    sum += a
    print("{:6}".format(a), end="")
    if flag % 5 == 0:
        print()
    flag += 1
    a += 1
if flag % 5 != 0:
    print()
print("Sum = " + str(sum))
