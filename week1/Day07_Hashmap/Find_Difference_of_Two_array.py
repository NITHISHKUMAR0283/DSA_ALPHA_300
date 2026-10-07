class Solution(object):
    def findDifference(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[List[int]]
        """
        Diff = [[] for _ in range(2)]
        seen1 = set()#unique ele from nums1
        seen2 = set()#unique ele from nums2
        for ele in nums1:
            seen1.add(ele)
        for ele in nums2:
            seen2.add(ele)
        #check if the ele from one array is not present in another and remove that element from the current seen so that duplicate are avoided
        for ele in nums1:
            if ele not in seen2 and ele in seen1:
                Diff[0].append(ele)
                seen1.discard(ele)

        for ele in nums2:
            if ele not in seen1 and ele in seen2:
                Diff[1].append(ele)
                seen2.discard(ele)
        return Diff
        