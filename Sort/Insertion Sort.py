array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

# 삽입 정렬 소스코드
for i in range(1, len(array)):
	# 인덱스 i부터 1까지 1씩 감소하면서 반복
	for j in range(i, 0, -1):
		# 한 칸씩 왼쪽으로 이동
		if array[j] < array[j - 1]:
			array[j], array[j - 1] = array[j - 1], array[j]
		else: break

print(array)