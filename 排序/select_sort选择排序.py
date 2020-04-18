# 设第一个元素为比较元素，依次和后面的元素比较，比较完所有元素找到最小的元素，将它和第一个元素互换
# 重复上述操作，我们找出第二小的元素和第二个位置的元素互换，以此类推找出剩余最小元素将它换到前面，即完成排序
import numpy as np


def select_sort(arr):
    for i in range(len(arr) - 1):
        min_index = 1
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[min_index], arr[i] = arr[i], arr[min_index]
    return arr


a = np.random.randint(0, 100, 20)
print(a)
b = select_sort(a)
print(b)
#
# 稳定性：因为存在任意位置的两个元素交换，比如[5, 8, 5, 2]，第一个5会和2交换位置，
# 所以改变了两个5原来的相对顺序，所以为不稳定排序。