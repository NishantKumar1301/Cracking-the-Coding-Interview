"""Question7 : Rotate Matrix: Given an image represented by an NxN matrix, where each pixel
in the image is 4 bytes, write a method to rotate the image by 90 degrees. Can you do
this in place? Hints: #51, # 100"""

def rotate_matrix(matrix):
    n = len(matrix)
    for i in range(n):
        for j in range(i+1,n):
            matrix[i][j],matrix[j][i]=matrix[j][i],matrix[i][j]

    for i in range(n):
        matrix[i].reverse()
    return matrix

# input_matrix = [
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9]
# ]

n = int(input("Enter the size of the matrix (N): "))
input_matrix = []
print(f"Enter the  value  of the {n}x{n} matrix:(Row wise)")
for _ in range(n):
    row_entry = list(map(int,input().split()))
    input_matrix.append(row_entry)

print(rotate_matrix(input_matrix))