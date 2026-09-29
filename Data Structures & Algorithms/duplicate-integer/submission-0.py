class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        Hashset=set()
        for n in nums:#iterate in list
            if n  in Hashset:# if found the same element which is inisde set 
                return True  #it is duplicate
            Hashset.add(n) #adding the unique elements
        return False #tells there are no duplicates

