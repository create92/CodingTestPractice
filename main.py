def dfs(graph, v, visited):
	# 현재 노드를 방문 처리
	visited[v] = True
	print(v, end = ' ')

	# 현재 노드와 연결된 다른 노드를 재귀적으로 방문
	for i in graph[v]:
		if not visited[i]:
			dfs(graph, i, visited) 


# 입력 및 함수 검증

# 각 노드가 연결되 정보를 표현 (2차원 리스트)

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

dfs(graph, 1, visited)

