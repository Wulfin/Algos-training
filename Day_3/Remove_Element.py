from typing import List


class Solution(object):
    def removeElement(self, nums, val):
        length = len(nums)
        for i in range(length):
            if nums[i] == val:
                nums = nums[:i] + nums[i + 1:]
                nums.append("")

        return nums, length - nums.count("")


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    solution = Solution()
    result = solution.removeElement([3,2,2,3], 3)
    print(result)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
