# 2869번

# 달팽이는 올라가고 싶다

# 문제

# 땅 위에 달팽이가 있다. 이 달팽이는 높이가 V미터인 나무 막대를 올라갈 것이다.

# 달팽이는 낮에 A미터 올라갈 수 있다. 하지만, 밤에 잠을 자는 동안 B미터 미끄러진다. 또, 정상에 올라간 후에는 미끄러지지 않는다.

# 달팽이가 나무 막대를 모두 올라가려면, 며칠이 걸리는지 구하는 프로그램을 작성하시오.

# 입력
# 첫째 줄에 세 정수 A, B, V가 공백으로 구분되어서 주어진다. (1 ≤ B < A ≤ V ≤ 1,000,000,000)

# 출력
# 첫째 줄에 달팽이가 나무 막대를 모두 올라가는데 며칠이 걸리는지 출력한다.

# 예제 입력 1 
# 2 1 5
# 예제 출력 1 
# 4
# 예제 입력 2 
# 5 1 6
# 예제 출력 2 
# 2
# 예제 입력 3 
# 100 99 1000000000
# 예제 출력 3 
# 999999901

import math

A, B, V = map(int, input().split())
day_count = 0

daily_distance = A-B
remaining_distance = V - A


if A >= V :
    day_count = 1
else:
    remaining_distance/daily_distance
    if isinstance(remaining_distance/daily_distance, int) == False:
        day_count = math.ceil(remaining_distance/daily_distance) + 1 
    else:
        pass 

print(day_count)

# 생각을 해보자
# 불쌍한 달팽이는 하루에 A만큼 올라가고, 자는 동안 B만큼 미끄러지고, 최종적으로 Vm에 도달해야한다. 
# 식으로 나타내면? 
# 하루에 총 올라가는 거리 : (A-B)
# for문을 써보는 건 어떨까? 

# 맨 처음 아래처럼 풀었는데, 엄청 큰 수에 대해서 계산 시간이 너무 오래걸림 --> while문 반복으로 인해서..

# snail_fighting = 0
# day_counting = 0
# while snail_fighting < V:
#     if day_counting >= 1:
#         day_counting += 1 
#     snail_fighting += A
#     if snail_fighting >= V:
#         break
#     else:
#         snail_fighting -= B
#         day_counting += 1
    

# print(day_counting)

# 매일 순수하게 올라가는 높이 = A-B 
# V지점에 도달하기 직전까지는 V-A만큼의 거리를 이동해야함 
# 이 거리를 하루에 순수히 올라가는 높이로 나누면? 며칠 걸리는지 계산이 빡 될겨 

