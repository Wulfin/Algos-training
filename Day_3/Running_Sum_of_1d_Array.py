class Solution(object):
    def runningSum(self, nums):
        runningSum = []
        for i in range(len(nums)):
            sum = 0
            for j in range(i + 1):
                sum += nums[j]
            runningSum.append(sum)

        return runningSum


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    solution = Solution()
    print(solution.runningSum([1, 2, 3]))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
