d0 = [2, 15, 5, 9, 7, 6, 4, 12, 5, 4, 2, 64, 5, 6, 4, 2, 3, 54, 45, 4, 44]
d0_out = [2, 2, 2, 3, 4, 4, 4, 4, 5, 5, 5, 6, 6, 7, 9, 12, 15, 44, 45, 54, 64]

d_max = 0
d_min = 0
for i in d0:
    if d_max<i:
        d_max = i
    if d_min>i:
        d_min = i

d1 = {}
for i in d0:
    if i in d1.keys():
        d1[i] += 1
    else:
        d1[i] = 1

d2 = []
for i in range(d_min,d_max+1):
    if i in d1.keys():
        for j in range(d1[i]):
            d2.append(i)

print(d2)