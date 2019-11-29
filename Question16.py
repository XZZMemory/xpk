x = int(input())
if x < 15:
    cost = 4 * x / 3
else:
    cost = 2.5 * x - 17.5
print("{:.2f}".format(cost))
