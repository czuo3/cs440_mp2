# search.py
# ---------------
# Licensing Information:  You are free to use or extend this projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to the University of Illinois at Urbana-Champaign
#
# Created by Michael Abir (abir2@illinois.edu) on 08/28/2018

"""
This is the main entry point for MP1. You should only modify code
within this file -- the unrevised staff files will be used for all other
files and classes when code is run, so be careful to not modify anything else.
"""
# Search should return the path and the number of states explored.
# The path should be a list of tuples in the form (row, col) that correspond
# to the positions of the path taken by your search algorithm.
# Number of states explored should be a number.
# maze is a Maze object based on the maze from the file specified by input filename
# searchMethod is the search method specified by --method flag (bfs,dfs,greedy,astar)

def search(maze, searchMethod):
    return {
        "bfs": bfs,
        "dfs": dfs,
        "greedy": greedy,
        "astar": astar,
    }.get(searchMethod)(maze)


def bfs(maze):
    # TODO: Write your code here
    # return path, num_states_explored
    start_point=maze.getStart()
    row,col=maze.getDimensions()
    visited=[]
    previous=[]
    for i in range(row):
        visited.append([])
        previous.append([])
        for j in range(col):
            visited[i].append(False)
            previous[i].append((0,0))

    objectives=maze.getObjectives()
    obj_size=len(objectives)
    found=False
    visited[start_point[0]][start_point[1]]=True
    previous[start_point[0]][start_point[1]]=(start_point[0],start_point[1])
    reverse_path=[]
    path=[]
    q=[]
    q.append(start_point)
    num_states_explored=0
    while found==False:
        current_point=q[0]
        q.remove(current_point)
        corx=current_point[0]
        cory=current_point[1]
        neighbors=maze.getNeighbors(corx,cory)
        for i in range(len(neighbors)):
            neighbor=neighbors[i]
            for j in range(obj_size):
                if neighbor[0]==objectives[j][0] and neighbor[1]==objectives[j][1]:
                    previous[neighbor[0]][neighbor[1]]=(corx,cory)
                    it=neighbor
                    path.append(it)
                    while it!=start_point:
                        it=previous[it[0]][it[1]]
                        reverse_path.append(it)
                        print(it)
                    for i in range(len(reverse_path)):
                        path.append(reverse_path[len(reverse_path)-1-i])

                    return path, num_states_explored

            if visited[neighbor[0]][neighbor[1]]==False:
                visited[neighbor[0]][neighbor[1]]=True
                previous[neighbor[0]][neighbor[1]]=(corx,cory)
                q.append(neighbor)
                num_states_explored+=1


    return [], 0


def dfs(maze):
    # TODO: Write your code here
    # return path, num_states_explored
    start_point=maze.getStart()
    row,col=maze.getDimensions()
    visited=[]
    previous=[]
    for i in range(row):
        visited.append([])
        previous.append([])
        for j in range(col):
            visited[i].append(False)
            previous[i].append((0,0))

    objectives=maze.getObjectives()
    obj_size=len(objectives)
    found=False
    visited[start_point[0]][start_point[1]]=True
    previous[start_point[0]][start_point[1]]=(start_point[0],start_point[1])
    reverse_path=[]
    path=[]
    q=[]
    q.append(start_point)
    num_states_explored=0
    while found==False:
        current_point=q[len(q)-1]
        q.remove(current_point)
        corx=current_point[0]
        cory=current_point[1]
        neighbors=maze.getNeighbors(corx,cory)
        for i in range(len(neighbors)):
            neighbor=neighbors[i]
            for j in range(obj_size):
                if neighbor[0]==objectives[j][0] and neighbor[1]==objectives[j][1]:
                    previous[neighbor[0]][neighbor[1]]=(corx,cory)
                    it=neighbor
                    path.append(it)
                    while it!=start_point:
                        it=previous[it[0]][it[1]]
                        reverse_path.append(it)
                        print(it)
                    for i in range(len(reverse_path)):
                        path.append(reverse_path[len(reverse_path)-1-i])
                    return path, num_states_explored

            if visited[neighbor[0]][neighbor[1]]==False:
                visited[neighbor[0]][neighbor[1]]=True
                previous[neighbor[0]][neighbor[1]]=(corx,cory)
                q.append(neighbor)
                num_states_explored+=1


    return [], 0


def greedy(maze):
    # TODO: Write your code here
    # return path, num_states_explored
    start_point=maze.getStart()
    row,col=maze.getDimensions()
    visited=[]
    correct_path=[]
    examined=[]
    for i in range(row):
        visited.append([])
        examined.append([])
        for j in range(col):
            visited[i].append(False)
            examined[i].append(False)

    objectives=maze.getObjectives()
    obj_size=len(objectives)
    objective=objectives[0]
    visited[start_point[0]][start_point[1]]=True
    examined[start_point[0]][start_point[1]]=True
    current_point=start_point
    path=[]
    q=[]
    q.append(start_point)
    num_states_explored=0
    while len(q)!=0:
        distance=1000
        closest_idx=0
        print(current_point[0],current_point[1])
        for i in range(len(q)):
            new_distance=abs(q[i][0]-objective[0])+abs(q[i][1]-objective[1])
            if new_distance<distance:
                closest_idx=i
                distance=new_distance
                print(i)

        current_point=q[closest_idx]
        q.remove(current_point)
        corx=current_point[0]
        cory=current_point[1]
        if current_point==objective:
            print('666')
            examined[corx][cory]=True
            break

        else:

            neighbors=maze.getNeighbors(corx,cory)
            for i in range(len(neighbors)):
                neighbor=neighbors[i]
                if visited[neighbor[0]][neighbor[1]]==False:
                    visited[neighbor[0]][neighbor[1]]=True
                    q.append(neighbor)

            examined[corx][cory]=True

    for i in range(row):
        for j in range(col):
            print(i,j,examined[i][j])

    end_point=objective
    path.append(end_point)

    current_point=end_point
    num_states_explored+=1
    while current_point!=start_point:
        corx=current_point[0]
        cory=current_point[1]
        print(corx,cory)
        neighbors=maze.getNeighbors(corx,cory)
        if len(neighbors)==1 and examined[neighbors[0][0]][neighbors[0][1]]==False:
            print('first')
            path.remove(current_point)
            current_point=path[len(path)-1]
        elif len(neighbors)==2 and examined[corx][cory]==False:
            print('second')
            path.remove(current_point)
            current_point=path[len(path)-1]

        else:
            print('thrid')
            examined[corx][cory]=False
            has_examined=False
            for i in range(len(neighbors)):
                neighbor=neighbors[i]

                print(i)
                if examined[neighbor[0]][neighbor[1]]==True:
                    path.append(neighbor)
                    current_point=neighbor
                    num_states_explored+=1
                    has_examined=True
                    break
            if has_examined==False:
                path.remove(current_point)
                current_point=path[len(path)-1]
                print('no examined')

    for i in range(len(path)):
        correct_path.append(path[len(path)-1-i])

    return path, num_states_explored


def astar_single(maze):
    # TODO: Write your code here
    # return path, num_states_explored
    start_point=maze.getStart()
    row,col=maze.getDimensions()
    visited=[]
    previous=[]
    successorg=[]
    successorf=[]
    successorh=[]

    for i in range(row):
        visited.append([])
        successorg.append([])
        successorf.append([])
        successorh.append([])
        for j in range(col):
            visited[i].append(False)
            successorg[i].append(-1)
            successorf[i].append(-1)
            successorh[i].append(-1)

    objectives=maze.getObjectives()
    obj_size=len(objectives)
    found=False
    visited[start_point[0]][start_point[1]]=True
    successorg[start_point[0]][start_point[1]]=0
    path=[]
    q=[]
    q.append(start_point)
    num_states_explored=0
    while len(q)!=0:
        current_point=q[0]
        q.remove(current_point)
        corx=current_point[0]
        cory=current_point[1]
        neighbors=maze.getNeighbors(corx,cory)
        for i in range(len(neighbors)):
            neighbor=neighbors[i]
            if visited[neighbor[0]][neighbor[1]]==False:
                visited[neighbor[0]][neighbor[1]]=True
                successorg[neighbor[0]][neighbor[1]]=successorg[corx][cory]+1
                q.append(neighbor)

            else:
                if successorg[neighbor[0]][neighbor[1]]>successorg[corx][cory]+1:
                    successorg[neighbor[0]][neighbor[1]]=successorg[corx][cory]+1



    q=[]
    for i in range(row):
        for j in range(col):
            visited[i][j]=False

    if obj_size==1:
        end_point=objectives[0]
        q.append(end_point)
        successorf[end_point[0]][end_point[1]]=0
        visited[end_point[0]][end_point[1]]=True
        while len(q)!=0:
            current_point=q[0]
            q.remove(current_point)
            corx=current_point[0]
            cory=current_point[1]
            neighbors=maze.getNeighbors(corx,cory)
            for i in range(len(neighbors)):
                neighbor=neighbors[i]
                if visited[neighbor[0]][neighbor[1]]==False:
                    visited[neighbor[0]][neighbor[1]]=True
                    successorh[neighbor[0]][neighbor[1]]=successorh[corx][cory]+1
                    q.append(neighbor)

                else:
                    if successorh[neighbor[0]][neighbor[1]]>successorh[corx][cory]+1:
                        successorh[neighbor[0]][neighbor[1]]=successorh[corx][cory]+1


    for i in range(row):
        for j in range(col):
            visited[i][j]=False
            successorf[i][j]=successorg[i][j]+successorh[i][j]

    path=[]
    num_states_explored=0
    current_point=start_point
    visited[current_point[0]][current_point[1]]=True
    visited[1][1]=True
    path.append(start_point)
    while found==False:
        corx=current_point[0]
        cory=current_point[1]
        neighbors=maze.getNeighbors(corx,cory)
        neighborf=100000
        neighbor_idx=5

        for i in range(len(neighbors)):
            neighbor=neighbors[i]
            if visited[neighbor[0]][neighbor[1]]==False:
                visited[neighbor[0]][neighbor[1]]=True
                if neighbor==objectives[0]:
                    path.append(neighbor)
                    num_states_explored+=1
                    print('ass')
                    return path,num_states_explored

                if successorf[neighbor[0]][neighbor[1]]<neighborf:
                    neighborf=successorf[neighbor[0]][neighbor[1]]
                    neighbor_idx=i
                elif successorf[neighbor[0]][neighbor[1]]==neighborf:
                    if successorh[neighbor[0]][neighbor[1]]<successorh[corx][cory]:
                        neighbor_idx=i

        path.append(neighbors[neighbor_idx])
        current_point=neighbors[neighbor_idx]
        num_states_explored+=1


    return [], 0

def astar(maze):
    # TODO: Write your code here
    # return path, num_states_explored
    start_point=maze.getStart()
    row,col=maze.getDimensions()
    objectives=maze.getObjectives()
    points=objectives
    distance=[]
    visited=[]
    previous=[]
    successorf=[]
    successorg=pre_astar(maze,objectives)
    for m in range(row):
        successorf.append([])
        distance.append([])
        for n in range(col):
            successorf[m].append([])
            distance[m].append([])
            for i in range(row):
                successorf[m][n].append([])
                distance[m][n].append([])
                visited.append([])
                for j in range(col):
                    distance[m][n][i].append(-1)
                    successorf[m][n][i].append(-1)
                    visited[i].append(-1)
    distance_points=[]
    distance_points.append(start_point)
    for i in range(len(objectives)):
        distance_points.append(objectives[i])

    for i in range(len(distance_points)):
        for j in range(len(distance_points)):
            if i!=j:
                distance[distance_points[i][0]][distance_points[i][1]][distance_points[j][0]][distance_points[j][1]]=bfs_astar(maze,distance_points[i],distance_points[j])

    shortest_interval=10000
    interval_dict={}
    current_point=start_point
    simple_path=[]
    points=objectives
    sorted_list=[]
    temp_points=()
    visited_points=[]
    while len(points)!=0:
        for idx_a in range(len(points)):
    		interval_dict[[current_point,points[idx_a]]=distance[current_point[0]][current_point[1]][points[idx_a][0]][points[idx_a][1]]
    	current_point=points[0]
        points.remove(points[0])
    ##print(interval_dict)
    interval_list=interval_dict.values
    while len(interval_list)!=0:
    	for idx_b in range(len(interval_list)):
    		if interval_list[idx_b]<shortest_interval:
    			shortest_interval=interval_list[idx_b]
    	sorted_list.append(shortest_interval)
    	interval_list.remove(shortest_interval)
    	shortest_interval=10000
    while len(sorted_list)!=0:
    	for x,y in interval_dict.items():
    		if y=sorted_list[0]: ##get two points with shortest interval
    			#now we should check two points in x, 3 case
    			# 1 simply add to temp_points tuple
    			# 2 one of the point already in temp_tuple and not in visited list so should be added to visited and the two
    			# points should be added to simple path
    			# 3 second time we have one of point in x in temp tuple, should ignore
    			for z in temp_points:
    				if x[0]==z[0]:
    					for w in visited_points:
    						if w == x[0]:
    							ignore==True
    						else:
    							ignore==False
    					if ignore==False
    						if len(simple_path)==0
    							simple_path.append(z[1])
    							simple_path.append(z[0])
    							simple_path.append(x[1])
    							visited_points.append[x[0]]
    							visited_points.append[z[1]]
    							temp_points.append(x)
    						else:
    							simple_path.append(x[1])
    							visited_points.append[x[0]]
    							temp_points.append(x)
    				if x[1]==z[1]:
    					for w in visited_points:
    						if w == x[1]:
    							ignore==True
    						else:
    							ignore==False
    					if ignore==False
    						if len(simple_path)==0
    							simple_path.append(z[0])
    							simple_path.append(z[1])
    							simple_path.append(x[0])
    							visited_points.append[z[0]]
    							visited_points.append[z[1]]
    							temp_points.append(x)
    						else:
    							simple_path.append(x[0])
    							visited_points.append[x[1]]
    							temp_points.append(x)
    				else:
    					temp_points.append(x)
    	sorted_list.remove[sorted_list[0]]





    for i in range(row):
        for j in range(col):
            visited[i][j]=False

    path=[]
    num_states_explored=0
    current_point=start_point
    current_start=start_point
    current_goal=simple_path[1]
    goal_idx=1
    visited[current_point[0]][current_point[1]]=True
    visited_goal=[]
    visited_goal.append(start_point)
    path.append(start_point)
    get_to_new_goal=False
    while current_start!=simple_path[len(simple_path)-1]:

        if get_to_new_goal==True:
            #print('current_start',current_start)
            #print('current_goal',current_goal)

            get_to_new_goal=False
            for i in range(row):
                for j in range(col):
                    visited[i][j]=False
            #for i in range(len(visited_goal)):
                #visited[visited_goal[i][0]][visited_goal[i][1]]=True
                #print(visited_goal[i])

        corx=current_point[0]
        cory=current_point[1]
        neighbors=maze.getNeighbors(corx,cory)
        neighborf=100000
        neighbor_idx=0
        #print('current',current_point)
        for i in range(len(neighbors)):
            neighbor=neighbors[i]
            #print(neighbor,visited[neighbor[0]][neighbor[1]])
            #print(current_point)
            #print(successorg[current_start[0]][current_start[1]][neighbor[0]][neighbor[1]])
            if visited[neighbor[0]][neighbor[1]]==False:
                #print('ttttt',current_start)
                visited[neighbor[0]][neighbor[1]]=True
                if neighbor==current_goal:
                    visited_goal.append(neighbor)
                    #path.append(neighbor)
                    current_start=neighbor

                    neighbor_idx=i
                    get_to_new_goal=True
                    if (goal_idx+1)==len(simple_path):
                        for i in range(len(path)):
                            print('path',path[i])
                        path.append(current_goal)
                        return path,num_states_explored
                    else:
                        goal_idx+=1
                        current_goal=simple_path[goal_idx]
                    break

                if successorg[current_start[0]][current_start[1]][neighbor[0]][neighbor[1]]+successorg[current_goal[0]][current_goal[1]][neighbor[0]][neighbor[1]]<neighborf:
                    neighborf=successorg[current_start[0]][current_start[1]][neighbor[0]][neighbor[1]]+successorg[current_goal[0]][current_goal[1]][neighbor[0]][neighbor[1]]
                    neighbor_idx=i
                    #print('second',current_start)

                elif successorg[current_start[0]][current_start[1]][neighbor[0]][neighbor[1]]+successorg[current_goal[0]][current_goal[1]][neighbor[0]][neighbor[1]]==neighborf:
                    #print('third',current_start)
                    if successorg[current_goal[0]][current_goal[1]][neighbor[0]][neighbor[1]]<successorg[current_goal[0]][current_goal[1]][neighbors[neighbor_idx][0]][neighbors[neighbor_idx][1]]:
                        neighbor_idx=i

        path.append(neighbors[neighbor_idx])
        current_point=neighbors[neighbor_idx]

    return [], 0

def smallest_successorf(maze,start,objectives,successorg):
    smallest_f=100000
    smallest_idx=0
    for i in range(len(objectives)):
        successorf=successorg[start[0]][start[1]][objectives[i][0]][objectives[i][1]]+successorg[objectives[i][0]][objectives[i][1]][start[0]][start[1]]

        if successorf<smallest_f:
            smallest_f=successorf
            smallest_idx=i

    return objectives[smallest_idx],smallest_idx

def closest(maze,start,objectives,distance):
    smallest_distance=100000
    smallest_idx=0
    for i in range(len(objectives)):
        if distance[start[0]][start[1]][objectives[i][0]][objectives[i][1]]<smallest_distance:
            smallest_distance=distance[start[0]][start[1]][objectives[i][0]][objectives[i][1]]
            smallest_idx=i

    return objectives[smallest_idx],smallest_idx

def bfs_astar(maze,start_point,end_point):
    # TODO: Write your code here
    # return path, num_states_explored
    row,col=maze.getDimensions()
    visited=[]
    previous=[]
    for i in range(row):
        visited.append([])
        previous.append([])
        for j in range(col):
            visited[i].append(False)
            previous[i].append((0,0))

    found=False
    visited[start_point[0]][start_point[1]]=True
    previous[start_point[0]][start_point[1]]=(start_point[0],start_point[1])
    reverse_path=[]
    path=[]
    q=[]
    q.append(start_point)
    num_states_explored=0
    while len(q)!=0:
        current_point=q[0]
        q.remove(current_point)
        corx=current_point[0]
        cory=current_point[1]
        neighbors=maze.getNeighbors(corx,cory)
        for i in range(len(neighbors)):
            neighbor=neighbors[i]

            if neighbor[0]==end_point[0] and neighbor[1]==end_point[1]:
                previous[neighbor[0]][neighbor[1]]=(corx,cory)
                it=neighbor
                path.append(it)
                while it!=start_point:
                    it=previous[it[0]][it[1]]
                    reverse_path.append(it)
                    #print(it)
                for i in range(len(reverse_path)):
                    path.append(reverse_path[len(reverse_path)-1-i])

                return len(path)

            if visited[neighbor[0]][neighbor[1]]==False:
                visited[neighbor[0]][neighbor[1]]=True
                previous[neighbor[0]][neighbor[1]]=(corx,cory)
                q.append(neighbor)
                num_states_explored+=1


    return [], 0

def pre_astar(maze,objectives):
    # TODO: Write your code here
    # return path, num_states_explored
    start_point=maze.getStart()
    row,col=maze.getDimensions()
    points=[]
    points.append(start_point)
    for i in range(len(objectives)):
        points.append(objectives[i])

    visited=[]
    successorg=[]
    for m in range(row):
        successorg.append([])
        for n in range(col):
            successorg[m].append([])
            for i in range(row):
                successorg[m][n].append([])
                for j in range(col):
                    successorg[m][n][i].append(-1)


    for i in range(row):
            visited.append([])
            for j in range(col):
                visited[i].append(False)
    for p in range(len(points)):
        for k in range(row):
            for j in range(col):
                visited[k][j]=False

        visited[points[p][0]][points[p][1]]=True
        successorg[points[p][0]][points[p][1]][points[p][0]][points[p][1]]=0
        q=[]
        q.append(points[p])
        num_states_explored=0
        while len(q)!=0:
            current_point=q[0]
            q.remove(current_point)
            corx=current_point[0]
            cory=current_point[1]
            neighbors=maze.getNeighbors(corx,cory)
            for i in range(len(neighbors)):
                neighbor=neighbors[i]
                if visited[neighbor[0]][neighbor[1]]==False:
                    visited[neighbor[0]][neighbor[1]]=True
                    successorg[points[p][0]][points[p][1]][neighbor[0]][neighbor[1]]=successorg[points[p][0]][points[p][1]][corx][cory]+1
                    q.append(neighbor)

                else:
                    if successorg[points[p][0]][points[p][1]][neighbor[0]][neighbor[1]]>successorg[points[p][0]][points[p][1]][corx][cory]+1:
                        successorg[points[p][0]][points[p][1]][neighbor[0]][neighbor[1]]=successorg[points[p][0]][points[p][1]][corx][cory]+1



    return successorg
