"""Question8: Zero Matrix: Write an algorithm such that if an element in an MxN matrix is 0,
its entire row and column are set to 0. Hints:#17, #74, #702"""

def set_zero_matrix(matrix):
    if not matrix :
        return None
    rows_to_zero= set()
    cols_to_zero = set()
    n = len(matrix)
    for i in range(n):
        for j in range(len(matrix[i])):
            if matrix[i][j]==0:
                rows_to_zero.add(i)
                cols_to_zero.add(j)
                

    for i in rows_to_zero:
        for j in range(n):
            matrix[i][j]=0


    for i in cols_to_zero:
        for j in range(n):
            matrix[j][i]=0 

    return matrix

# input_matrix = [
#     [1, 2, 3],
#     [4, 0, 6],
#     [7, 8, 9]
# ]

m, n = map(int, input("Enter the number of rows (M) and columns (N): ").split())

input_matrix = []
print(f"Enter the {m}x{n} matrix rows:")
for _ in range(m):
    row = list(map(int, input().split()))  
    input_matrix.append(row)

print(set_zero_matrix(input_matrix))