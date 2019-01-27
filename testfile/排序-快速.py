def quick_sort(alist, start, end):
    """快速排序"""
    if start >= end:
        return
    # 基准
    mid = alist[start]
    # 左边游标
    left = start
    # 右边游标
    right = end

    while left < right:
        while left < right and alist[right] >= mid:
            # 右边游标移动，左边游标不动
            right -= 1
        alist[left] = alist[right]
        while left < right and alist[left] < mid:
            # 左边游标移动，右边游标不动
            left += 1
        alist[right] = alist[left]
    # 退出循环后 left与right重合，即相等
    alist[left] = mid
    # 递归的方式排左边的序列
    quick_sort(alist, start, left - 1)
    # 递归的方式排右边的序列
    quick_sort(alist, left + 1, end)


if __name__ == '__main__':
    alist = [54, 26, 93, 17, 77, 31, 44, 55, 20]
    print("原列表为：%s" % alist)
    quick_sort(alist, 0, len(alist) - 1)
    print("新列表为：%s" % alist)