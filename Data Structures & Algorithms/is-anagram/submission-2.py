class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        mapS = {}

        for i in range(len(s)):
            mapS[s[i]] = mapS.get(s[i],0) + 1
            mapS[t[i]] = mapS.get(t[i],0) - 1

        for count in mapS.values():
            if count > 0:
                return False

        return True