#BFS
frontier = {1:(2,3),2:(4,7),3:(8,9),4:(),7:(),8:(),9:()}
cpy = list(frontier)
print(frontier)
flag = 0
explored = []
for key in frontier:
    break
goal = int(input("Enter a node to search :"))
if key == goal:
    print(key,"\n Found")
for key in cpy:
    if(cpy==[]):
        print("Tree is empty")
        break
    explored.append(key)
    frontier.pop(key)
    if(key == goal):
        print(key,"\nFound")
        flag = 1
        break
    else:
        print(key)

if(flag == 0):
    print("Not found")
