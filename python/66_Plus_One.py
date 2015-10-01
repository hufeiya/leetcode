class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        digits[len(digits)-1] += 1
        for i in range(len(digits))[::-1]:
            if i != 0:
                if digits[i] == 10:
                    digits[i] = 0
                    digits[i-1] += 1
            else:
                if digits[i] == 10:
                    digits[i] = 0
                    digits = [1] + digits
        return digits
                
