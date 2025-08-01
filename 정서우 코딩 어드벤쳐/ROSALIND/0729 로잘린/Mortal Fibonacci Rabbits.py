# Mortal Fibonacci Rabbits

# Wabbit Season

# Problem

# Figure 4. A figure illustrating the propagation of Fibonacci's rabbits if they die after three months.
# Recall the definition of the Fibonacci numbers from “Rabbits and Recurrence Relations”, which followed the recurrence relation Fn = Fn−1 + Fn−2
# and assumed that each pair of rabbits reaches maturity in one month and produces a single pair of offspring (one male, one female) each subsequent month.

# Our aim is to somehow modify this recurrence relation to achieve a dynamic programming solution in the case that all rabbits die out after a fixed number of months. See Figure 4 for a depiction of a rabbit tree in which rabbits live for three months (meaning that they reproduce only twice before dying).

# Given: Positive integers n≤100
# and m≤20.

# Return: The total number of pairs of rabbits that will remain after the n
# -th month if all rabbits live for m
#  months.

# Sample Dataset
# 6 3

# Sample Output
# 4

# 중간에 포기하고 gemini가 풀어줌 ㅠ 복습하자


def solve_mortal_rabbits(n, m):
    # 각 달마다의 토끼 나이별 개수를 저장하는 배열
    # age[i]는 i개월 차의 토끼 수 (0개월 ~ m-1개월까지 존재)
    age = [0] * m
    age[0] = 1  # 첫 달에 1쌍 태어남

    for month in range(1, n):
        # 새로 태어나는 토끼 = 나이 1개월 이상된 토끼들의 총합
        new_borns = sum(age[1:])
        # 나이 한 달씩 증가 → 맨 뒤는 죽고, 맨 앞(0개월)은 새로 태어난 애들로 채움
        age = [new_borns] + age[:-1]

    return sum(age)


# 입력 예시: 사용자에게서 n, m을 받아서 실행
n, m = map(int, input().split())
print(solve_mortal_rabbits(n, m))
