class Solution:
    # @return a tuple, (index1, index2)
    def twoSum(self, num, target):
        index = 0
        hashit=  {} # hash sheet
        for i in xrange(len(num)):
            second = target - num[i]
            if second in hashit:
                return (hashit[second] + 1,i + 1)
            hashit[num[i]] = i
