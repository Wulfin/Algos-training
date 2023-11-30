class Solution(object):
    def intersect(self,nums1, nums2):
        intersection = []

        for i in nums1:
            for j in range(0, len(nums2)):
                if nums2[j] == i:
                    nums2 = nums2[0: j] + nums2[j+1:]
                    intersection.append(i)
                    break

        return intersection


if __name__ == '__main__':
    solution = Solution()
    result = solution.intersect([1, 2, 2], [2, 2])
    print(result)
