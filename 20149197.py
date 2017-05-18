v,e,start = map(int, input().split())
adj = [[0 for i in range(v+1)] for i in range(v+1)]


for _ in range(e):
    e1, e2 = map(int,input().split())
    adj[e1][e2] = adj[e2][e1] = 1

visited_DFS = [0 for _ in range(v+1)]
st = [start]
dfs =[]
bfs = []

while(st):
    now = st.pop()

    if(visited_DFS[now] == 0):
        dfs.append(now)
        visited_DFS[now] = 1

    for i in range(v, 0, -1):
        if(adj[now][i] == 1 and visited_DFS[i] == 0):
            st.append(i)

q = [start]
visited_BFS = [0 for _ in range(v+1)]

while(q):
    now = q.pop(0)
    if(now == start):
        visited_BFS[now] = 1
        bfs.append(now)

    for i in range(v+1):
        if(adj[now][i] == 1 and visited_BFS[i] == 0):
            q.append(i)
            visited_BFS[i] = 1
            bfs.append(i)

print(" ".join(map(str, dfs)))
print(" ".join(map(str, bfs)))
