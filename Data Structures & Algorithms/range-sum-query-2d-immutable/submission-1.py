class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.prefix = []
        rows, cols = len(matrix), len(matrix[0]) 
        for i in range(rows):
            arr = []
            total = 0
            for j in range(cols):
                total += matrix[i][j]
                arr.append(total)
            self.prefix.append(arr)

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        res = 0
        for i in range(row1, (row2+1)):
            right_sum = self.prefix[i][col2]
            left_sum = self.prefix[i][col1-1] if col1 > 0 else 0
            res += (right_sum - left_sum)
        return res

        


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)