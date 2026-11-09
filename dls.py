def bfs(graph,start_node):
    visited=[]
    stack=[start_node]
    while stack:
        current_node=stack.pop()
        if current_node not in visited:
            visited.append(current_node)
        for neighbour in graph.get(current_node,[]):
            if neighbour not in visited and neighbour not in stack:
                stack.append(neighbour)       
    return visited
 
    




print(".......build your graph.......")
student_graph={}
edges=int(input("enter number of edges you need :"))
for i in range(edges):
    u,v=input(f"edes{i+1}:").split()
    if u not in student_graph:
        student_graph[u]=[]
    if v not in student_graph:
        student_graph[v]=[]        
    student_graph[u].append(v)
    student_graph[v].append(u)
start=input("enter your start node : ")
print("graph:-",student_graph)
a=bfs(student_graph,start)
print("visited list:",a)

