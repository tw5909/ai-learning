x = float(input("请输入 x："))
y = 0

for i in range(1, 31):
    y = y + x ** i

print("计算结果是：", y)
