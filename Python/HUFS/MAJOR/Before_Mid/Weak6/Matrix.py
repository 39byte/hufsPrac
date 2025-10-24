class Matrix:
    def __init__(self, data):
        self.matrix = data
        self.row_len = len(data)
        self.col_len = len(data[0])

    def Add(self, other):   #행렬 합
        out = self.matrix[:]
        for i in range(self.row_len):
            for j in range(self.col_len):
                out[i][j] = self.matrix[i][j] + other.matrix[i][j]
        return Matrix(out)
    
    def Matmul(self, other):    #행렬 곱
        out = [[0] * other.col_len for i in range(self.row_len)]

        if self.col_len != other.row_len:   #각각 행과 열이 같지 않으면 내뱉기
            print("행렬의 row와 cols가 일치하지 않습니다.")
            return
        
        for i in range(self.row_len):
            for h in range(self.row_len):
                for j in range(self.col_len):
                    out[i][h] += self.matrix[i][j] * other.matrix[j][h]
        return Matrix(out)
    
    def Print(self):    #행렬 출력
        return "[" + "\n".join("[" + " ".join(f"{v:6.1f}" for v in row) + "]" for row in self.matrix) + "]"
    
    def transpose(self):
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

print("row num : \n", A.row_len)
print("col num : \n", A.col_len)
print("A : \n", A.matrix)

print(A.Print())
print(B.Print())

# print("\nA + B : \n", A.Add(B).Print())

# print("\nA T : \n", A.transpose().Print())


A = Matrix([[1, 2, 3], 
            [4, 5, 6]])

C = Matrix([[1, 2], 
            [3, 4], 
            [5, 6]])

print(A.Print())
print(C.Print())
print("\nA * C : \n", A.Matmul(C).Print())