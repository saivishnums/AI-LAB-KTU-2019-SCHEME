def is_safe(graph, v, color, c):
    for i in range(len(graph)):
        if graph[v][i] == 1 and color[i] == c:
            return False
    return True

def solve_graph_coloring_util(graph, m, color, v, V):
    if v == V:
        return True
    for c in range(1, m + 1):
        if is_safe(graph, v, color, c):
            color[v] = c
            if solve_graph_coloring_util(graph, m, color, v + 1, V):
                return True
            color[v] = 0
    return False

def graph_coloring(graph, m):
    V = len(graph)
    color = [0] * V
    if not solve_graph_coloring_util(graph, m, color, 0, V):
        print("Solution does not exist")
        return False
    print("Solution Exists: Following are the assigned colors")
    print(" ".join(map(str, color)))
    return color
if __name__ == '__main__':
    graph = [
        [0, 1, 1, 1],
        [1, 0, 1, 0],
        [1, 1, 0, 1],
        [1, 0, 1, 0],
    ]
    m = 3
    graph_coloring(graph, m)
