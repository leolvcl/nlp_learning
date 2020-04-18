# 从第一个和第二个开始比较，如果第一个比第二个大，则交换位置，然后比较第二个和第三个，逐渐往后
# 经过第一轮后最大的元素已经排在最后，所以重复上述操作的话第二大的则会排在倒数第二的位置。
# 那重复上述操作n-1次即可完成排序，因为最后一次只有一个元素所以不需要比较
import numpy as np

def bubble_sort(arr):
    for i in range(len(arr) - 1):
        for j in range(len(arr) - 1 - i):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr

# a = np.random.randint(0,100,100)
# print(a)
# b = bubble_sort(a)
# print(b)