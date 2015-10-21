class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        hashmap = {}
        for i in xrange(len(nums)):
            if nums[i] not in hashmap:
                hashmap[nums[i]] = i
            elif i - hashmap[nums[i]] <= k:
                return True
            else:
                hashmap[nums[i]] = i
        return False
