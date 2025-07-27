#Then there are n lines of m characters describing the labyrinth. Each character is . (floor), # (wall), A (start), or B (end). There is exactly one A and one B in the input.
labyrinthe= [["#","#","#","#","#","#","#","#"],
["#" ,".","A","#",".",".",".","#"],
["#",".","#","#",".","#","B","#"],
["#",".",".",".",".",".",".","#"],
["#","#","#","#","#","#","#","#"]]

def labyrinth(lab):
    length = 0 
    directions=""
    
    dir = [(-1, 0, "U"), (1,0,"D"), (0,1,"R"), (0,-1,"L")]
   
    n= len(lab)
    m = len(lab[0])
    a, b =  [(i, j) for i, row in enumerate(lab) 
                    for j, element in enumerate(row) 
                    if element == "A"][0]
    x, y= [(i, j) for i, row in enumerate(lab) 
                    for j, element in enumerate(row) 
                    if element == "B"][0]
    stack = [(a,b,"")]
    visited= set((a,b))
    while stack :
        v ,w,e= stack.pop()
        if (v,w)==(x,y):
            return f"YES\n{len(e)}\n{e}"
        for r,l,o in dir :
            X = v + r 
            Y = w + l 
            if (0<=X<n and 0<=Y<m and lab[X][Y] in [".","B"] and (X,Y) not in visited):
                visited.add((X,Y))
                
                stack.append((X,Y,e+o))
    return "NO"
print(labyrinth(labyrinthe))
    