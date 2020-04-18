def direct_insertion_sort(d):  # 直接插入排序，因为要用到后面的希尔排序，所以转成function
    d1 = [d[0]]
    for i in d[1:]:
        state = 1
        for j in range(len(d1) - 1, -1, -1):
            if i >= d1[j]:
                d1.insert(j + 1, i)  # 将元素插入数组
                state = 0
                break
        if state:
            d1.insert(0, i)
    return d1


def shell_sort(d):  # d 为乱序数组，l为初始增量,其中l<len(d),取为len(d)/2比较好操作。最后还是直接省略length输入
    length = int(len(d) / 2)  # 10
    num = int(len(d) / length)  # 2
    while 1:

        for i in range(length):
            d_mid = []
            for j in range(num):
                d_mid.append(d[i + j * length])
            d_mid = direct_insertion_sort(d_mid)
            for j in range(num):
                d[i + j * length] = d_mid[j]
        # print(d)
        length = int(length / 2)
        if length == 0:
            return d
            break
        # print('length:',length)
        num = int(len(d) / length)


if __name__ == "__main__":
    d0 = [2, 15, 5, 9, 7, 6, 4, 12, 5, 4, 2, 64, 5, 6, 4, 2, 3, 54, 45, 4, 44]  # 原始乱序
    d0_out = [2, 2, 2, 3, 4, 4, 4, 4, 5, 5, 5, 6, 6, 7, 9, 12, 15, 44, 45, 54, 64]  # 正确排序
    d1 = shell_sort(d0)
    print(d1)
    print(d0_out)