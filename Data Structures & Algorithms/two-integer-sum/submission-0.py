class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        a=[]
        for i,n in enumerate(nums):
            a.append([n,i])
        a.sort()
        i,j=0,len(nums)-1

        while(i<j):
            curr=a[i][0]+a[j][0]
            if curr==target:
                return [min(a[i][1],a[j][1]),max(a[i][1],a[j][1])]
            elif curr>target:
                j-=1
            else:
                i+=1
        return []