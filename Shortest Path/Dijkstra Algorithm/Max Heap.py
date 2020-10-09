# 파이썬에서 기본적으로 제공하는 힙 라이브러리는 Min Heap 최소힙을 제공함 따라서 Max Heap을 구현하려고 하면, 부호를 반대로 입력하여 구현하여야 함.
import heapq

# 오름차순 힙 정렬(Heap Sort)
def heapsort(iterable):
	h = []
	result = []

	# 모든 원소를 차례대로 힙에 삽입
	for value in iterable:
		heapq.heappush(h, -value)
	
	# 힙에 삽입된 모든 원소를 차례대로 꺼내어 담기
	for i in range(len(h)):
		result.append(-heapq.heappop(h))
	
	return result

result = heapsort([1,3,5,7,9,2,4,6,8,0])
print(result)