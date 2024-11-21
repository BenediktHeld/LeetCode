def quicksort(nums):
    """
    Sortiert eine Liste von Zahlen mithilfe des Quicksort-Algorithmus.

    :param nums: Eine Liste von Zahlen
    :return: Die sortierte Liste
    """
    if len(nums) <= 1:
        return nums

    pivot = nums[len(nums) // 2]
    left = [x for x in nums if x < pivot]
    middle = [x for x in nums if x == pivot]
    right = [x for x in nums if x > pivot]

    return quicksort(left) + middle + quicksort(right)


class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """

        nums1 = nums1 + nums2
        nums1 = quicksort(nums1)

        if len(nums1)%2==0:
            ersteZahl = (int(len(nums1)/2)-1)
            zweiteZahl = int(ersteZahl + 1)
            median = float(nums1[ersteZahl]+nums1[zweiteZahl])/2
            return median
        else:
            median = nums1[len(nums1)/2]
            return median

nums1 = [1,2]
nums2 = [3,4]
print(Solution().findMedianSortedArrays(nums1,nums2))

