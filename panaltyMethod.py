import math

maxsize = float('inf')

def copyToFinal(curr_path):
    final_path[:N + 1] = curr_path[:]
    final_path[N] = curr_path[0]

def firstMin(adj, i, visited):
    min_val = maxsize
    for k in range(N):
        if adj[i][k] < min_val and i != k and not visited[k]:
            min_val = adj[i][k]
    return min_val

def secondMin(adj, i, visited):
    first, second = maxsize, maxsize
    for j in range(N):
        if i == j or visited[j]:
            continue
        if adj[i][j] <= first:
            second = first
            first = adj[i][j]
        elif adj[i][j] <= second:
            second = adj[i][j]
    return second

def TSPRec(adj, curr_bound, curr_weight, level, curr_path, visited):
    global final_res

    if level == N:
        if adj[curr_path[level - 1]][curr_path[0]] != 0:
            curr_res = curr_weight + adj[curr_path[level - 1]][curr_path[0]]
            if curr_res < final_res:
                copyToFinal(curr_path)
                final_res = curr_res
        return

    for i in range(N):
        if adj[curr_path[level - 1]][i] != 0 and not visited[i]:
            temp = curr_bound
            curr_weight += adj[curr_path[level - 1]][i]

            if level == 1:
                curr_bound -= (firstMin(adj, curr_path[level - 1], visited) + firstMin(adj, i, visited)) / 2
            else:
                curr_bound -= (secondMin(adj, curr_path[level - 1], visited) + firstMin(adj, i, visited)) / 2

            if curr_bound + curr_weight < final_res:
                curr_path[level] = i
                visited[i] = True
                TSPRec(adj, curr_bound, curr_weight, level + 1, curr_path, visited)

            curr_weight -= adj[curr_path[level - 1]][i]
            curr_bound = temp
            visited = [False] * len(visited)
            for j in range(level):
                if curr_path[j] != -1:
                    visited[curr_path[j]] = True

def TSP(adj):
    global N, final_res, final_path
    N = len(adj)
    curr_bound = 0
    curr_path = [-1] * (N + 1)
    visited = [False] * N

    for i in range(N):
        curr_bound += (firstMin(adj, i, visited) + secondMin(adj, i, visited))

    curr_bound = math.ceil(curr_bound / 2)

    visited[0] = True
    curr_path[0] = 0
    final_res = maxsize

    TSPRec(adj, curr_bound, 0, 1, curr_path, visited)


adj = [[0, 600, 1000, 1900, 1100],
       [600, 0, 1900, 1900, 1500],
       [1000, 1900, 0, 1700, 1200],
       [1900, 1900, 1700, 0, 1900],
       [1100, 1500, 1200, 1900, 0]]

N = 5

 
final_path = [None] * (N + 1)
visited = [False] * N
final_res = maxsize

TSP(adj)

city_names = ['a', 'b', 'c', 'd', 'e']

print("Minimum cost:", final_res)
print("Path Taken:", end=' ')
for i in range(N + 1):
    print(city_names[final_path[i]], end='  ')