class Solution:
    def trap(self, height: List[int]) -> int:
        n=len(height)
        water=0
        for i in range(n):
            leftMax = rightMax= height[i]
            for j in range(i):
                leftMax=max(leftMax,height[j])
            for j in range(i+1,n):
                rightMax=max(rightMax,height[j])
            water+=min(rightMax,leftMax)-height[i]
        return water
        