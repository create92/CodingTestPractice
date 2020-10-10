# 소수 판별 : 개선된 알고리즘
'''
< 개선된 알고리즘의 기본 원리 >
- 자연수의 약수가 가지는 특징을 이용
- 약수들을 쭉 나열했을 때, 가운데 약수를 기준으로 해서 각 등식이 대칭적인 형태를 보임
- 따라서, 우리는 바로 가운데 약수까지만 '나누어 떨어지는지' 확인해보면 됨
- 이를 통해, 전체 for문으로 돌리는게 아니라 효율적으로 알고리즘을 개선할 수 있음
'''

import math

# 소수 판별 함수 (2이상의 자연수에 대하여)
def is_prime_number(x):
	# 2부터 x의 제곱근까지의 모든 수를 확인하며
	for i in range(2, int(math.sqrt(x))+ 1):
		# x가 해당 수로 나누어떨어진다면
		if x % i == 0:
			# 소수가 아님
			return False
	# 소수임
	return True

print(is_prime_number(4))
print(is_prime_number(7))