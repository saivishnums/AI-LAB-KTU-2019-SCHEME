def a_star_search(graph, heuristic, start, goal):
    visited = set()
    to_visit = {start: heuristic[start]}  # f(n) = g(n) + h(n)
    g_cost = {start: 0}
    parent = {}

    while to_visit:
        current = min(to_visit, key=to_visit.get)
        print(f"Visiting: {current}")

        if current == goal:
            path = [current]
            while current in parent:
                current = parent[current]
                path.append(current)
            path.reverse()
            print("Path found:", " -> ".join(path))
            print(f"Total cost: {g_cost[goal]}")
            return

        visited.add(current)
        to_visit.pop(current)

        for neighbor, cost in graph.get(current, {}).items():
            if neighbor in visited:
                continue
            tentative_g = g_cost[current] + cost
            if neighbor not in g_cost or tentative_g < g_cost[neighbor]:
                g_cost[neighbor] = tentative_g
                f_cost = tentative_g + heuristic.get(neighbor,0)
                to_visit[neighbor] = f_cost
                parent[neighbor] = current

    print("Goal not found.")


graph = {}
heuristic = {}

n = int(input("How many nodes? "))
for _ in range(n):
    node = input("\nEnter node name: ")
    graph[node] = {}
    neighbors = input(f"Enter neighbors of {node} with cost (format: B:4 C:2): ").split()
    for item in neighbors:
        if ':' in item:
            neighbor, cost = item.split(":")
            graph[node][neighbor] = int(cost)

print("\nEnter heuristic values:")
for node in graph:
    heuristic[node] = int(input(f"Heuristic for {node}: "))

start = input("\nStart node: ")
goal = input("Goal node: ")

print("\n--- A* Search ---")
a_star_search(graph, heuristic, start, goal)
