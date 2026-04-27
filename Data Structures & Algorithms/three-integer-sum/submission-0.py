class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        n=len(nums)
        output=[]
        for i in range (n):
            if i>0 and nums[i]==nums[i-1]:
                continue
            target = -nums[i]
            l,r=i+1,n-1
            while l<r:
                sum=nums[l]+nums[r]
                if sum<target:
                    l+=1
                elif sum>target:
                    r-=1
                else:
                    output.append([nums[i],nums[l],nums[r]])
                    l+=1
                    r-=1
                    while l < r and nums[l] == nums[l-1]:
                        l += 1
                    while l < r and nums[r] == nums[r+1]:
                        r -= 1
        return output


                