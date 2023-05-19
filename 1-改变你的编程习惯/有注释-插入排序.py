def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]  # 当前要插入的元素
        j = i - 1     # 已排序区间的最后一个元素下标
        while j >= 0 and key < arr[j]:  # 在已排序区间中查找位置
            arr[j + 1] = arr[j]        # 右移元素，空出插入位置
            j -= 1                     # 继续向前寻找插入位置
        arr[j + 1] = key  # 插入元素到正确位置

if __name__ == "__main__":
    arr = [3, 5, 2, 7, 6, 1, 4]
    insertion_sort(arr)  # 调用函数进行排序
    print(arr)           # 输出排序后的结果
