def removeDuplicates(nums):
    if len(nums) == 0: return 0
    if len(nums) == 1: return 1

    i = 0
    while i < len(nums)-1:
        if nums[i] == nums[i+1]:
            nums.pop(i)
        else:
            i += 1

    return i+1


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print(removeDuplicates([1,2,3,3,3,3,4,5]))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
