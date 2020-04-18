# import sys
# sys.setrecursionlimit(1000000)

def quick_sort(data):
    d = [[], [], []]
    d_pivot = data[-1]  # 因为是乱序数组，所以第几个都是可以的，理论上是一样的
    for i in data:
        if i < d_pivot:  # 小于基准值的放在前
            d[0].append(i)
        elif i > d_pivot:  # 大于基准值的放在后
            d[2].append(i)
        else:  # 等于基准值的放在中间
            d[1].append(i)

    # print(d[0], d[1], d[2])
    if len(d[0]) > 1:  # 大于基准值的子数组，递归
        d[0] = quick_sort(d[0])

    if len(d[2]) > 1:  # 小于基准值的子数组，递归
        d[2] = quick_sort(d[2])

    d[0].extend(d[1])
    d[0].extend(d[2])
    return d[0]


if __name__ == "__main__":
    d0 = [2, 15, 5, 9, 7, 6, 4, 12, 5, 4, 2, 64, 5, 6, 4, 2, 3, 54, 45, 4, 44]  # 原始乱序
    d0_out = [2, 2, 2, 3, 4, 4, 4, 4, 5, 5, 5, 6, 6, 7, 9, 12, 15, 44, 45, 54, 64]  # 正确排序
    d1 = quick_sort(d0)
    print(d1)
    print(d0_out)