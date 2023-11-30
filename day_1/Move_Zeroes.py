def Move_Zeroes(nums):
    index = 0
    for i in range(len(nums)):
        if nums[index] == 0:
            nums.pop(index)
            nums.append(0)
        else: index += 1
    return nums


if __name__ == '__main__':
    print(Move_Zeroes([1, 3, 4, 0, 9, 9, 0, 0, 9]))
