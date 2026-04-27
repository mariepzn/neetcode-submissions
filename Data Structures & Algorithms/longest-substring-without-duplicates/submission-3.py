class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_len=0
        n=len(s)
        sub=""
        begin=0
        i=0
        while i<n:
            if s[i] not in sub:
                sub+=s[i]
                max_len=max(max_len,len(sub))
                i+=1
            else:
                sub=""
                i=begin+1
                begin+=1
                


        
        return max_len



        