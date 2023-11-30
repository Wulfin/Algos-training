def removeDuplicates(nums):
    if len(nums) == 0: return 0
    if len(nums) == 1: return 1

    dict = {}
    i = 0
    while i < len(nums):
        if nums[i] in dict.keys():
            if dict[nums[i]] == 1:
                dict[nums[i]] = 2
                i += 1
            else: nums.pop(i)
        else:
            dict[nums[i]] = 1
            i += 1

    return sum(dict.values())


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print(removeDuplicates([1,2,2,2,3,3,4]))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
