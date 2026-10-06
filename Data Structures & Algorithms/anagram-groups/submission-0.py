class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        #you need a defualt dict while taking a list as argument
        r=defaultdict(list)
        for s in strs:
            count=[0]*26
            for c in s:
                count[ord(c)-ord('a')]+=1
            
            r[tuple(count)].append(s)
        return list(r.values())