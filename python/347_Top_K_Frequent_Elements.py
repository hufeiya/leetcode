class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        hashmap = {}
        for i in nums:
            hashmap[i]=hashmap[i] + 1 if i in hashmap else  1
        sort = sorted(hashmap.items(),key=lambda e: e[1],reverse=True)
        result = []
        for i,j in sort[:k]:
            result.append(i)
        return result
