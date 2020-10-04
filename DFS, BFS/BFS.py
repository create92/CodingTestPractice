from collections import deque

# BFS 메서드 정의
def bfs(graph, start, visited):
	# 큐(Queue) 구현을 위해 deque 라이브러리 사용
	queue = deque([start])

	# 현재 노드를 방문 처리
	visited[start] = True

	# 큐가 빌때까지 반복
	while queue:
		# 큐에서 하나의 원소를 뽑아 출력하기
		v = queue.popleft()
		print(v, end= ' ')
		# 아직 방문하지 않은 인접ㅎ한 원소들을 큐에 삽입
		for i in graph[v]:
			if not visited[i]:
				queue.append(i)
				visited[i] = True


graph = [
		 [],		# 0번 노드(노드가 1부터 시작하는 경우가 많아서 비워놓고 하는게[ 코드 구현할때 직관적으로 좋음]) 
		 [2, 3, 8], # 1번 노드
		 [1, 7], 	# 2번 노드
		 [1, 4, 5], # 3번 노드
		 [3, 5], 	# 4번 노드
		 [3, 4], 	# 5번 노드
		 [7], 		# 6번 노드
		 [2, 6, 8], # 7번 노드
		 [1, 7]		# 8번 노드
		 ]

# 각 노드가 방문된 정보를 표현 (1차원 리스트)
#  0-노드, 1-노드, 2-노드, 3-노드,  4-노드, 5-노드, 6-노드, 7-노드, 8-노드
# [False, False, False, False, False, False, False, False, False]
visited = [False] * 9

bfs(graph, 1, visited)