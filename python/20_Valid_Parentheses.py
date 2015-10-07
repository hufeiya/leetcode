class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if len(s) % 2:
            return False
        hashTable = {'(':')','[':']','{':'}'}
        stack = []
        for i in s:
            if i in hashTable:
                stack.append(i)
            elif len(stack) == 0 or hashTable[stack[-1]] != i:
                return False
            else:
                stack.pop()
        return len(stack) == 0
