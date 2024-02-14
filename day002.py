def dfs(g, i, visited):
    visited[i] = 1
    print(chr(ord('A')+i), end=' ')
    for j in range(len(g)):
        if g[i][j] == 1 and not visited[j]:
            dfs(g, j, visited)

'''
G1 = Graph(5)
G1.graph[0][2] = 1; G1.graph[0][3] = 1
G1.graph[1][2] = 1
G1.graph[2][0] = 1; G1.graph[2][1] = 1; G1.graph[2][3] = 1
G1.graph[3][0] = 1; G1.graph[3][2] = 1
G1.graph[4][2] = 1; G1.graph[4][3] = 1
'''

graph = [
    [0, 1, 0, 1, 0],
    [1, 0, 1, 1, 0],
    [0, 1, 0, 0, 1],
    [1, 1, 0, 0, 1],
    [0, 0, 1, 1, 0]
]


visited = [0] * len(graph)
dfs(graph, 0, visited)
