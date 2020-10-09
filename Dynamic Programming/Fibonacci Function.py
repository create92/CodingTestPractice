# 피보나치 함수(Fibonacci Function)을 재귀 함수로 구현
def fibo(x):
	if x == 1 or x == 2:
		return 1
	return fibo(x - 1) + fibo(x - 2)

print(fibo(4))

# 피보나치 함수(Fibonacci Function) 메모이제이션 기법으로 구현

# 한 번 계산된 결과를 메모이제이션(Memoization)하기 위한 리스트 초기화
d = [0] * 100

# 피보나치 함수(Fibonacci Function)를 재귀함수로 구현(탑다운 다이내믹 프로그래밍)
def fibonacci(x):
	# 종료 조건(1, 2일때 1을 반환)
	if x == 1 or x == 2:
		return 1
	
	# 이미 계산한 적 있는 문제라면 그대로 반환
	if d[x] != 0:
		return d[x]
	
	# 아직 계산하지 않은 문제라면 점화식에 따라서 피보나치 결과 반환
	d[x] = fibonacci(x - 1) + fibonacci(x - 2)
	return d[x]

print(fibonacci(99))

