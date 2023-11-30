def Majority_Element(nums):
    mid = len(nums) // 2
    counts = {}
    majority = nums[0]
    majorityCount = 0

    for n in nums:
        if n not in counts.keys():
            counts[n] = 1
        else:
            counts[n] += 1

        if counts[n] >= mid:
            if counts[n] > majorityCount:
                majorityCount, majority = counts[n], n

    if majorityCount == 0:
        return None
    else:
        return majority


if __name__ == '__main__':
    print(Majority_Element([1, 3, 4, 4, 4, 4, 5, 5]))
