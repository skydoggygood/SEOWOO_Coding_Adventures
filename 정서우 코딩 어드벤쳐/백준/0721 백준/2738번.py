# 2738번

# 문제
# N*M크기의 두 행렬 A와 B가 주어졌을 때, 두 행렬을 더하는 프로그램을 작성하시오.

# 입력
# 첫째 줄에 행렬의 크기 N 과 M이 주어진다. 둘째 줄부터 N개의 줄에 행렬 A의 원소 M개가 차례대로 주어진다. 이어서 N개의 줄에 행렬 B의 원소 M개가 차례대로 주어진다. N과 M은 100보다 작거나 같고, 행렬의 원소는 절댓값이 100보다 작거나 같은 정수이다.

# 출력
# 첫째 줄부터 N개의 줄에 행렬 A와 B를 더한 행렬을 출력한다. 행렬의 각 원소는 공백으로 구분한다.

# 예제 입력 1
# 3 3
# 1 1 1
# 2 2 2
# 0 1 0
# 3 3 3
# 4 4 4
# 5 5 100
# 예제 출력 1
# 4 4 4
# 6 6 6
# 5 6 100

# 이건 진짜 gemini가 다풀었음 행렬 너무 어려움 진짜로

N, M = map(int, input().split())

matrix_A = []
matrix_B = []

for i in range(N):
    a = map(int, input().split())
    matrix_A.append(list(a))

for j in range(N):
    b = map(int, input().split())
    matrix_B.append(list(b))

result_matrix = []


for _ in range(N):
    result_matrix.append([])

for row in range(N):
    for col in range(M):
        sum_element = matrix_A[row][col] + matrix_B[row][col]
        result_matrix[row].append(sum_element)

for row in range(N):
    for col in range(M):
        print(result_matrix[row][col], end=" ")
    print()
