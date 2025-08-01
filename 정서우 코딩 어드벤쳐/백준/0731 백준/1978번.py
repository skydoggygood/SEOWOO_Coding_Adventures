# 1978번

# 소수 찾기

# 문제
# 주어진 수 N개 중에서 소수가 몇 개인지 찾아서 출력하는 프로그램을 작성하시오.

# 입력
# 첫 줄에 수의 개수 N이 주어진다. N은 100이하이다. 다음으로 N개의 수가 주어지는데 수는 1,000 이하의 자연수이다.

# 출력
# 주어진 수들 중 소수의 개수를 출력한다.

# 예제 입력 1
# 4
# 1 3 5 7
# 예제 출력 1
# 3

N = int(input())

numbers = list(map(int, input().split()))

if len(numbers) > N:
    print("error")
else:
    pass

prime_count = 0

for num in numbers:
    is_prime = True
    if num < 2:
        is_prime = False
    else:
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                is_prime = False
                break
    if is_prime:
        prime_count += 1

print(prime_count)
