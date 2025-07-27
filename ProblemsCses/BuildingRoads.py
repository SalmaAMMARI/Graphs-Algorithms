cities={1:[2], 2:[1], 3:[4], 4:[3]}
num_cities = len(cities)
num_edges=2

#connectd is a fct that finds all the connected parts of the graph
def connected(cities):
    graphs=[]
    visited = {i: False for i in cities}    
    for city in cities:
        if not visited[city]:
            visited[city]=True
            subGraph = []
            stack=[city ]
            while stack:
                ciity=stack.pop()
                subGraph.append(ciity)
                for neighbor in cities[ciity]:
                    if not visited[neighbor]:
                        visited[neighbor]=True
                        stack.append(neighbor)
            graphs.append(subGraph)
    return graphs
graphs = connected(cities)
print(len(graphs)-1)
for i in range(len(graphs)):
    print(graphs[i][0])

