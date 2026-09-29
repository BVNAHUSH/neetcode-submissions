class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        Cs,Ct={},{}
        for i in range(len(s)):
            Cs[s[i]]=1+Cs.get(s[i],0)   #we can also write like this but Cs[s[i]]=1+Cs[s[i]] if the initial key doesnt match it may break the problem 
            Ct[t[i]]=1+Ct.get(t[i],0)
        return Cs==Ct