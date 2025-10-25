#DFS
frontier = {1: (2, 3),2: (4, 7),3: (8, 9),4: (),7: (),8: (),9: ()}
cpy = list(frontier)
print("Initial State Space (Tree):", frontier)
flag = 0
explored = []
for key in frontier:
    start = key
    break
goal = int(input("Enter a node to search: "))
if start == goal:
    print(start, "Found at root")
    flag = 1
else:
    stack = [start]
    while stack:
        node = stack.pop()
        explored.append(node)
        if node == goal:
            print(node, "Found")
            flag = 1
            break
        else:
            print("Visiting:", node)
        children = list(frontier.get(node, ()))
        for child in reversed(children):
            if child not in explored:
                stack.append(child)
if flag == 0:
    print("Not found")
