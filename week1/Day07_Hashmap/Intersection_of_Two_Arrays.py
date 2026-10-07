class Solution(object):
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        seen = set()
        # finding unique ele from nums1
        for ele in nums1:
            seen.add(ele)
        intersection = []
        # if it is present in seen then it is common on both array 
        for ele in nums2:
            if ele in seen:
                intersection.append(ele)
                seen.discard(ele)
        return intersection
        