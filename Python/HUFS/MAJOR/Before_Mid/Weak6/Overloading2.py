class Matrix:
    def __init__(self, data):
        self.matrix = data
        self.row_len = len(data)
        self.col_len = len(data[0])

    def __add__(self, other):
        out = [[0] * self.col_len for i in range(self.row_len)]
        for i in range(self.row_len):
            for j in range(self.col_len):
                out[i][j] = self.matrix[i][j] + other.matrix[i][j]
        return Matrix(out)
    
    def __mul__(self, other):
        out = [[0] * self.col_len for i in range(self.row_len)]
        for i in range(self.row_len):
            for j in range(self.col_len):
                out[i][j] = self.matrix[i][j] * other.matrix[i][j]
        return Matrix(out)
    
    def __matmul__(self, other):
        out = [[0] * other.col_len for i in range(self.row_len)]

        if self.col_len != other.row_len:   #각각 행과 열이 같지 않으면 내뱉기
            print("행렬의 row와 cols가 일치하지 않습니다.")
            return
        
        for i in range(self.row_len):
            for h in range(self.row_len):
                s = 0
                for j in range(self.col_len):
                    s += self.matrix[i][j] * other.matrix[j][h]
                out[i][h] = s
        return Matrix(out)
    
    def __str__(self):
        return "[" + "\n".join("[" + " ".join(f"{v:6.1f}" for v in row) + "]" for row in self.matrix) + "]"
    
    @property
    def T(self):
        out = [[0] * self.row_len for i in range(self.col_len)]

        for i in range(self.row_len):
            for j in range(self.col_len):
                out[j][i] = self.matrix[i][j]
        return Matrix(out)
    

A = Matrix([[1, 2, 3], 
            [4, 5, 6]])

B = Matrix([[7, 8, 9], 
            [10, 11, 12]])

C = Matrix([[1, 2], 
            [3, 4]])

D = Matrix([[1, 2], 
            [3, 4], 
            [5, 6]])

print("\nA + B :", (A + B))
print("\nA * B :", (A * B))
print("\nA @ D :", (A @ D), end='\n\n')
print(A.T)