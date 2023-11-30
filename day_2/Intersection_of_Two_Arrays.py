class Solution(object):
    @staticmethod
    def intersection(nums1: list[int], nums2):
        intersection = []

        for i in nums1:
            if i in nums2:
                if i not in intersection:
                    intersection.append(i)

        return intersection


if __name__ == '__main__':
    result = Solution.intersection([1, 2], [2])
    print(result)
