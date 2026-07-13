class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        lengthM = len(matrix)
        lengthN = len(matrix[0])
        for m in matrix:
            bottom = 0
            top = lengthN - 1
            while bottom <= top :
                middle = int(top + bottom)//2 
                if m[middle] == target:
                    return True
                elif m[middle] < target:
                    bottom = middle + 1
                else:
                    top = middle - 1
        return False
