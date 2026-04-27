class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        l,r=0,len(matrix)-1
        while l<=r:
            m=l+((r-l)//2)
            if l==r:
                L,R=0,len(matrix[0])-1
                while L<=R:
                    M= L+((R-L)//2)
                    if matrix[l][M]==target:
                        return True
                    elif matrix[l][M]<target:
                        L=M+1
                    elif matrix[l][M]>target:
                        R=M-1
                return False
            else:
                if matrix[m][0]>target:
                    r=m-1
                elif matrix[m][len(matrix[0])-1]<target:
                    l=m+1
                else:
                    l = r = m   
         
        return False