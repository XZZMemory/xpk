'''计算下列分段函数f(x)的值'''
x = float(input())
if x == 0:
    fx = 0
else:
    fx = 1 / x
print('f({:.1f}) = {:.1f}'.format(x, fx))
