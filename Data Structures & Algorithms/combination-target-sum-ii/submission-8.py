class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        out=[]
        subset=[]
        candidates.sort()
        def dfs(i,s):
            if s==target:
                out.append(subset.copy())
                return
            if i==len(candidates) or s>target:
                return
            subset.append(candidates[i])
            s+=candidates[i]
            dfs(i+1,s)
            var=subset.pop()
            s-=var
            while i+1<len(candidates) and candidates[i]==candidates[i+1]:
                i+=1
            dfs(i+1,s)
        dfs(0,0)
        return out
