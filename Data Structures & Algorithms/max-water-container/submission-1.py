class Solution:
    def maxArea(self, heights: List[int]) -> int:
        n=len(heights)
        m=0 
        for l in range(n):  
            for j in range (l+1,n):
                height=min(heights[l],heights[j])
                length=j-l
                if height*length>m:
                    m=height*length
        return m   