class Solution(object):
    def getHint(self, secret, guess):
        """
        :type secret: str
        :type guess: str
        :rtype: str
        """
        bull,cow = 0,0
        rightMap = {}
        for i in xrange(len(secret)):
            if secret[i] == guess[i]:
                bull += 1
            elif secret[i] in rightMap:
                rightMap[secret[i]] += 1
            else:
                rightMap[secret[i]] = 1
        for i in xrange(len(secret)):
            if secret[i] != guess[i] and guess[i]  in rightMap:
                cow += 1
                rightMap[guess[i]] -= 1
                if rightMap[guess[i]] == 0:
                    rightMap.pop(guess[i])
        return str(bull)+"A"+str(cow)+"B"




from collections import Counter
from itertools import imap

class Solution2(object):
    def getHint(self, secret, guess):
        """
        :type secret: str
        :type guess: str
        :rtype: str
        """
        A = sum(imap(operator.eq, secret, guess))
        B = sum((Counter(secret) & Counter(guess)).values()) - A
        return "%dA%dB" % (A, B)


