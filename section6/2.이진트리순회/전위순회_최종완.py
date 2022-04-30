import sys


# 그래프 초기화
graph = [None] * 8
visitied = [False] * len(graph)

graph[1] = (2, 3)
graph[2] = (1,4,5)
graph[3] = (1,3,6,7)
graph[4] = (2)
graph[5] = (2)
graph[6] = (3)
graph[7] = (3)


#전위순회 실시
start = 1

for target in range(start, len(graph)):
    if not visitied[target]:
        visitied[target] = True
        print(target, end=' ')

    for child in graph[target]:
        if visitied[child]:
            continue
        else:
            print(child, end=' ')
            visitied[child] = True
