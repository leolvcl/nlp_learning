# 从第二个元素开始和前面的元素进行比较，如果前面的元素比当前元素大，则将前面元素 后移，当前元素依次往前，直到找到比它小或等于它的元素插入在其后面
#
# 然后选择第三个元素，重复上述操作，进行插入
#
# 依次选择到最后一个元素，插入后即完成所有排序

def direct_insertion_sort(d):   # 直接插入排序，因为要用到后面的希尔排序，所以转成function
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


if __name__ == "__main__":
    d0 = [2, 15, 5, 9, 7, 6, 4, 12, 5, 4, 2, 64, 5, 6, 4, 2, 3, 54, 45, 4, 44]  # 原始乱序
    d0_out = [2, 2, 2, 3, 4, 4, 4, 4, 5, 5, 5, 6, 6, 7, 9, 12, 15, 44, 45, 54, 64]  # 正确排序
    d1 = direct_insertion_sort(d0)
    print(d1)
    print(d0_out)