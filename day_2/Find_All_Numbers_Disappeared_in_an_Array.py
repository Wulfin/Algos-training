def findDisappearedNumbers(nums):
    """numsNotAppeared = [i for i in range(1, len(nums) + 1)]

    for num in nums:
        if num in numsNotAppeared:
            numsNotAppeared.remove(num)

    return numsNotAppeared"""
    for i in range(0, len(nums)):
        if nums[i]<0:
            numberAtIndex_i = -nums[i]
        else:
            numberAtIndex_i = nums[i]
        if nums[numberAtIndex_i - 1] > 0:
            nums[numberAtIndex_i - 1] *= -1

    numsNotAppeared = []
    for i in range(0, len(nums)):
        if nums[i] > 0:
            numsNotAppeared.append(i + 1)

    return numsNotAppeared


if __name__ == '__main__':
    print(findDisappearedNumbers([1, 3, 3, 2]))
