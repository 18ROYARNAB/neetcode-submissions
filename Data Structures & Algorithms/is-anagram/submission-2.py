class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
            
        counts={}
        for i in range (len(s)):
            c1=s[i]
            c2=t[i]

            counts[c1]=counts.get(c1,0)+1

            counts[c2]=counts.get(c2,0)-1

        for count in counts.values():
             if count != 0:
                return False
            
        return True