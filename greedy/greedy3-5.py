'''
<문제> 곱하기 혹은 더하기:문제 조건
입력조건 : 첫째 줄에 여러 개의 숫자로 구성된 하나의 문자열 S가 주어집니다.
(1 <= S의 길이 <= 20)

출력조건 : 첫째 줄에 만들어질 수 있는 가장 큰 수를 출력합니다.
'''

# 해결법 
# 0이 들어온 경우, 곱하면 값이 0이 되기 때문에 무조건 더해줌
# 1이 들어온 경우, 곱하면 값이 그대로이기 때문에 더해줘서 증가시켜줌
# 시작은 항상 0으로 
# 길이 1 이상 20 이상인 경우

input = str(input())

totalSum = 0

if input.len() < 1 || input.len() > 20:
  print("입력값 유효성 체크 다시 확인바람(1 이상 20 이하)")
else:
  for char in input:
      if char == "0" or char == "1":
        totalSum += int(char)
      else:
        totalSum *= int(char)

print(totalSum)
       

# 해답
data = input()

# 첫 번째 문자를 숫자로 변경하여 대입
result = int(data[0])

for i in range(1, len(data)):
  # 두 수 중에서 하나라도 '0' 혹은 '1'인 경우, 곱하기 보다는 더하기 수행
  num = int(data[i])
  if num <= 1 or result <= 1:
    result += num
  else:
    result 8= num

print(result)
