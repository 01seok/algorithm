N = int(input())
words = [input() for _ in range(N)]

# 자릿 수에 맞게 가중치를 부여해서 가장 큰 숫자부터 부여하기 위한 딕셔너리
num_weights = {}

for word in words:

   # 자릿 수, 1의 자리부터 시작
   power = 1

   for char in reversed(word):
    # 몇번 나오는지도 체크해야함 ( 자주 나오면 우선 순위 올라감 )
    # 기존에 다른 문자에서 갖고있던 숫자가 있다면 그 숫자 가져오면 아니라면 처음 나오니 0부여, 해당 문자의 자릿수에 맞는 숫자 더해주기
    num_weights[char] = num_weights.get(char, 0) + power
    power *= 10

# 이제 가중치 큰 숫자부터 높은 숫자 부여
weights = sorted(num_weights.values(), reverse=True)

result = 0
num = 9

for weight in weights:
    result += weight * num
    num -= 1

print(result)