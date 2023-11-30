class Solution(object):
    def pivotIndex(self, nums):
        i = 0
        while sum(nums[0:i]) != sum(nums[i + 1:]):
            i += 1
            if i == len(nums):
                return -1
        return i


if __name__ == '__main__':
    solution = Solution()
    nums = [2, 1, -1]
    result = solution.pivotIndex(nums)
    print(result)
