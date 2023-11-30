def two_sum(nums, target):
    for i in range(len(nums)):
        for j in range(len(nums)):
            if nums[i] + nums[j] == target:
                if i == j: continue
                return i, j


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print(two_sum([3,3], 6))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
