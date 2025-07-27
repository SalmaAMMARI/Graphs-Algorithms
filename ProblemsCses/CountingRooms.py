
building = [["#" ,"#" , "#","#","#","#","#","#"],["#",".",".","#",".",".",".","#"],["#" ,"#","#" ,"#",".","#",".","#"],["#",".",".","#",".",".",".","#"],["#","#","#","#","#","#","#","#"]]

for row in building:
    print(row) 

n=len(building)
m=len(building[0])
def count_rooms(building):
         
    room=0
 
    directions = [(-1, 0), (1,0), (0,1), (0,-1)]
   
    for i in range(len(building)):
        for j in range(len(building[0])):
            if building[i][j]==".":
                room+=1
                
                building[i][j]='#'
                stack = [(i,j)]
                while stack:
                    x , y = stack.pop()
                    for k , p in directions:
                        if (0<=k+x<n and 0<=p+y<m and building[k+x][p+y]=="."):
                            building[k+x][p+y]="#"
                            stack.append((k+x, p+y))
    return room


print(count_rooms(building))