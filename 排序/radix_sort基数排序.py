d0 = [2, 15, 5, 9, 7, 6, 4, 12, 5, 4, 2, 64, 5, 6, 4, 2, 3, 54, 45, 4, 44]

d1 = [[] for x in range(10)]

# 第一次 最小位次排序
for i in d0:
    d1[i % 10].append(i)

print(d1)

d0_1 = []
for i in d1:
    if i:
        for j in i:
            d0_1.append(j)
print(d0_1)

# 第二次 次低位排序
d2 = [[] for x in range(10)]
for i in d0_1:
    d2[int(i/10)].append(i)
print(d2)

d0_2 = []
for i in d2:
    if i:
        for j in i:
            d0_2.append(j)
print(d0_2)