d0 = [2, 15, 5, 9, 7, 6, 4, 12, 5, 4, 2, 64, 5, 6, 4, 2, 3, 54, 45, 4, 44]

d1 = [[] for x in range(10)]
for i in d0:
    d1[int(i/10)].append(i)

# print(d1)


for i in range(len(d1)):
    if d1[i] != []:
        d2 = [[] for x in range(10)]
        for j in d1[i]:
            d2[j%10].append(j)
        d1[i] = d2

# print(d1)

d3 = []
for i in d1:
    if i:
        for j in i:
            if j:
                for k in j:
                    if k:
                        d3.append(k)
print(d3)