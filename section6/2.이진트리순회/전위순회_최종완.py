

# 그래프 초기화
graph = [None] * 8
visitied = [False] * len(graph)

graph[1] = [2, 3]
graph[2] = [1,4,5]
graph[3] = [1,3,6,7]
graph[4] = [2]
graph[5] = [2]
graph[6] = [3]
graph[7] = [3]


#전위순회 실시
def dfs(start, graph, visitied):
    if not visitied[start]: print(start, end=' ')
    visitied[start] = True

    for child in graph[start]:
        if visitied[child]: continue
        visitied[child] = True

        print(child, end=' ')
        dfs(child, graph, visitied)

    

dfs(1, graph, visitied)