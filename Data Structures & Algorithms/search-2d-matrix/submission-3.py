class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        top, bottom = 0 , len(matrix)-1

        while top <= bottom:
            mid_list = (top+bottom)//2

            if matrix[mid_list][0] <= target:
                top = mid_list+1
            else: 
                bottom = mid_list-1
        
        if bottom<0:
            return False
        
        left , right = 0, len(matrix[bottom])-1

        while left <= right:
            mid = (left+right)//2

            if matrix[bottom][mid] == target:
                return True

            if matrix[bottom][mid] < target:
                left = mid+1
            else:
                right = mid-1
            
        return False
        

            
        




        