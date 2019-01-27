def merge_sort(alist):
    """归并排序"""
    n = len(alist)
    # 列表中只有一个元素
    if n == 1:
        return alist
    # 找到中间位置的角标
    mid = n // 2
    # 对分割后的左半部分进行拆分
    left_sorted_li = merge_sort(alist[:mid])
    for x in left_sorted_li:
        print("左半边=", x, end=" ")
    print(" ")
    # 对分割后的右半部分进行拆分
    right_sorted_li = merge_sort(alist[mid:])
    for y in right_sorted_li:
        print("右半边=", y, end=" ")
    print(" ")
    return merge(left_sorted_li, right_sorted_li)


# 以下代码是做归并排序，并进行最后序列的合并
def merge(left_sorted_li, right_sorted_li):
    # 先定义左右的游标，都从起始位置0开始
    left, right = 0, 0
    merge_result_li = []

    left_n = len(left_sorted_li)
    right_n = len(right_sorted_li)
    # 排序并合并
    while left < left_n and right < right_n:
        # 那边的元素小，就添加到新的列表中
        if left_sorted_li[left] <= right_sorted_li[right]:
            merge_result_li.append(left_sorted_li[left])
            left += 1
        else:
            merge_result_li.append(right_sorted_li[right])
            right += 1

    # 如果左半边或者右半边有一个先到末尾，上面的循环就退出了
    # 那么就把没有到末尾那半边的最后的元素添加到新的序列中，以免数值少算
    # 即使为null,会是空列表[],那么也没有关系，[1,2]+[]=[1,2]
    merge_result_li += left_sorted_li[left:]
    merge_result_li += right_sorted_li[right:]
    # 将合并后的新列表返回
    return merge_result_li


if __name__ == '__main__':
    alist = [54, 26, 93, 17, 77, 31, 44, 55, 20]
    print("原 alist: %s" % alist)
    sorted_alist = merge_sort(alist)
    print("排序后的 list ：%s" % sorted_alist)
