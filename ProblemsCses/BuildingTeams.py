friends= {1:[2,3], 2:[1], 3:[1], 4:[5], 5:[4]}

#a fct that finds all the connected teams in friends 

def connected(graph):
    if not graph:
        return []
    visited ={i:False for i in friends}
    result = []
    for  i in graph:
        if not visited[i]:
            visited[i]=True 
            subgraph=[]
            stack = [i]
            while stack:
                pupil = stack.pop()
                subgraph.append(pupil)
                for j in graph[pupil]:
                    if not visited[j]:
                        visited[j]=True 
                        stack.append(j)
            result.append(subgraph) 
    return result 
print(len(connected(friends)))
subgraphs=connected(friends)

print(connected(friends))
teams = []
for i in range(min(len(sub) for sub in subgraphs)):  # Éviter les index out of range
    team = []
    for sub in subgraphs:
        if i < len(sub):
            team.append(sub[i])  # Prend le i-ème joueur de chaque sous-graphe
        # Ou pour un choix aléatoire : team.append(random.choice(sub))
    teams.append(team)

print("Équipes formées :", teams)