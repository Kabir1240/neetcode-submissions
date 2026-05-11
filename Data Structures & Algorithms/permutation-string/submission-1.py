class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # Brute force. O(26*n*m) time and O(m^2 space).
        count = [0] * 26
        for i in s1:
            count[ord(i)-ord('a')] += 1
        
        for l in range(len(s2)):
            r = l + len(s1)
            selected = s2[l:r]

            if len(selected) != len(s1):
                break
            
            tempCount = [0] * 26
            for i in selected:
                tempCount[ord(i)-ord('a')] += 1
            
            for i in range(26):
                if tempCount[i] != count[i]:
                    break
                elif i == 25:
                    return True
        
        return False

