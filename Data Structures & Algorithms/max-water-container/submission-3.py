class Solution:
    def maxArea(self, heights: List[int]) -> int:
        n=len(heights)
        l,r=0,n-1
        m=0
        while l<r:
            height=min(heights[l],heights[r])
            length=r-l
            m=max(m,height*length)
            if heights[l]>heights[r]:
                r-=1
            else:
                l+=1
        return m   