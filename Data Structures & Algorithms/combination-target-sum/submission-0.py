class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        out=[]
        subset=[]
        s=0
        def dfs (i,s):
            if i >= len(nums):
                return
            if s>target:
                return
            if s==target:
                out.append(subset.copy())
                return
            
            subset.append(nums[i])
            s+=nums[i]
            dfs(i,s)
            var=subset.pop()
            s-=var
            dfs(i+1,s)


        dfs(0,s)
        return out
        