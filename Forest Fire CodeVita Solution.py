r,c = [int(x) for x in input().split(' ')]
start =[int(x)-1 for x in input().split(' ')]
forest = [[x for x in input().split(' ')] for _ in range(r)]
time = [[None for _ in range(c)] for _ in range(r)]
time[start[0]][start[1]] = 1
no_of_trees = 0
for i in range(r):
    for j in range(c):
        if forest[i][j] == 'T':
            no_of_trees+=1
queue=[]
queue.append(start)
trees_visited=0
p=[]
while queue:
    current = queue.pop(0)
    #print(current)
    x = current[0]
    y = current[1]
    curr_time = time[x][y]
    position=[]
    if x-1>=0 and x-1<r and y-1>=0 and y-1<c:
        if forest[x-1][y-1]!='W' and time[x-1][y-1]==None:
            position.append([x-1,y-1])
    if x>=0 and x<r and y-1>=0 and y-1<c:
        if forest[x][y-1]!='W' and time[x][y-1]==None:
            position.append([x,y-1])
    if x+1>=0 and x+1<r and y-1>=0 and y-1<c:
        if forest[x+1][y-1]!='W' and time[x+1][y-1]==None:
            position.append([x+1,y-1])
    if x-1>=0 and x-1<r and y>=0 and y<c:
        if forest[x-1][y]!='W' and time[x-1][y]==None:
            position.append([x-1,y])

    if x+1>=0 and x+1<r and y>=0 and y<c:
        if forest[x+1][y]!='W' and time[x+1][y]==None:
            position.append([x+1,y])
    if x-1>=0 and x-1<r and y+1>=0 and y+1<c:
        if forest[x-1][y+1]!='W' and time[x-1][y+1]==None:
            position.append([x-1,y+1])
    if x>=0 and x<r and y+1>=0 and y+1<c:
        if forest[x][y+1]!='W' and time[x][y+1]==None:
            position.append([x,y+1])
    if x+1>=0 and x+1<r and y+1>=0 and y+1<c:
        if forest[x+1][y+1]!='W' and time[x+1][y+1]==None:
            position.append([x+1,y+1])
    #print(position)
    
    for coord in position:
        j=coord[0]
        k=coord[1]
        time[j][k] = curr_time + 1
        queue.append(coord)
    
    trees_visited+=1
    if trees_visited==no_of_trees:
        break
#for i in p:
#    print(i)
for i in time:
    print(i)
            

        
    
