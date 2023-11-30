def merge(nums1, m, nums2, n):
    index1 = 0
    index2 = 0

    while index1 < m + n:
        if nums1[m - 1 + index2] <= nums2[index2]:
            nums1 = nums1[0: m + index2] + nums2[index2:]
            return nums1
        while nums1[index1] >= nums2[index2]:
            nums1.pop(-1)
            nums1 = nums1[0: index1] + [nums2[index2]] + nums1[index1:]
            index2 += 1
            if index2 == n: return nums1
        index1 += 1

    return nums1


if __name__ == '__main__':
    print(merge([1, 2, 3, 0, 0, 0], 3, [2, 5, 6], 3))
