# 5622번

# 문제
# 상근이의 할머니는 아래 그림과 같이 오래된 다이얼 전화기를 사용한다.


# 전화를 걸고 싶은 번호가 있다면, 숫자를 하나를 누른 다음에 금속 핀이 있는 곳 까지 시계방향으로 돌려야 한다. 숫자를 하나 누르면 다이얼이 처음 위치로 돌아가고, 다음 숫자를 누르려면 다이얼을 처음 위치에서 다시 돌려야 한다.

# 숫자 1을 걸려면 총 2초가 필요하다. 1보다 큰 수를 거는데 걸리는 시간은 이보다 더 걸리며, 한 칸 옆에 있는 숫자를 걸기 위해선 1초씩 더 걸린다.

# 상근이의 할머니는 전화 번호를 각 숫자에 해당하는 문자로 외운다. 즉, 어떤 단어를 걸 때, 각 알파벳에 해당하는 숫자를 걸면 된다. 예를 들어, UNUCIC는 868242와 같다.

# 할머니가 외운 단어가 주어졌을 때, 이 전화를 걸기 위해서 필요한 최소 시간을 구하는 프로그램을 작성하시오.

# 입력
# 첫째 줄에 알파벳 대문자로 이루어진 단어가 주어진다. 단어의 길이는 2보다 크거나 같고, 15보다 작거나 같다.

# 출력
# 첫째 줄에 다이얼을 걸기 위해서 필요한 최소 시간을 출력한다.

# 예제 입력 1
# WA
# 예제 출력 1
# 13
# 예제 입력 2
# UNUCIC
# 예제 출력 2
# 36

# alpha_num = list(input())  # WA

# # print(alpha_num)  # ['W', 'A']

# press_time = {
#     "ABC": 3,
#     "DEF": 4,
#     "GHI": 5,
#     "JKL": 6,
#     "MNO": 7,
#     "PQRS": 8,
#     "TUV": 9,
#     "WXYZ": 10,
#     "+-*/": 11,
# }

# total_time = []

# for i in range(len(alpha_num)):
#     if alpha_num[i] in "ABC":
#         total_time.append(press_time["ABC"])
#     elif alpha_num[i] in "DEF":
#         total_time.append(press_time["DEF"])
#     elif alpha_num[i] in "GHI":
#         total_time.append(press_time["GHI"])
#     elif alpha_num[i] in "JKL":
#         total_time.append(press_time["JKL"])
#     elif alpha_num[i] in "MNO":
#         total_time.append(press_time["MNO"])
#     elif alpha_num[i] in "PQRS":
#         total_time.append(press_time["PQRS"])
#     elif alpha_num[i] in "TUV":
#         total_time.append(press_time["TUV"])
#     elif alpha_num[i] in "WXYZ":
#         total_time.append(press_time["WXYZ"])
#     elif alpha_num[i] in "+-*/":
#         total_time.append(press_time["+-*/"])
#     else:
#         total_time.append(2)

# total_time = sum(total_time)

# print(total_time)

dial_time = {
    "A": 3,
    "B": 3,
    "C": 3,
    "D": 4,
    "E": 4,
    "F": 4,
    "G": 5,
    "H": 5,
    "I": 5,
    "J": 6,
    "K": 6,
    "L": 6,
    "M": 7,
    "N": 7,
    "O": 7,
    "P": 8,
    "Q": 8,
    "R": 8,
    "S": 8,
    "T": 9,
    "U": 9,
    "V": 9,
    "W": 10,
    "X": 10,
    "Y": 10,
    "Z": 10,
}

word = input().strip()
total_time = sum(dial_time[char] for char in word)
print(total_time)
