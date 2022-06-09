#Program for best first search

tree ={ 
    'A':[['B',3],['C',2]],
    'B':[['A',5],['C',2],['D',2],['E',3]],
    'C':[['A',5],['B',3],['F',2],['G',4]],
    'D':[['H',1],['I',99]],
    'F': [['J',99]],
    'G':[['K',99],['L',3]]
}

Start='A'
Goal='E'
Closed = []
SUCCESS=True
FAILURE=False
State=FAILURE

def MOVEGEN(N):
	New_list=list()
	if N in tree.keys():
		New_list=tree[N]
	
	return New_list
	
def GOALTEST(N):
	if N == Goal:
		return True
	else:
		return False

def APPEND(L1,L2):
	New_list=list(L1)+list(L2)
	return New_list
	
def SORT(L):
	L.sort(key = lambda x: x[1]) 
	return L 
	
def BestFirstSearch():
	OPEN=[[Start,5]]
	CLOSED=[]
	global State
	global Closed

	while (len(OPEN) != 0) and (State != SUCCESS):
		print("\n\n------------\n\n")
		N= OPEN[0]
		print("N=",N)
		del OPEN[0] #delete the node we picked
		
		if GOALTEST(N[0])==True:
			State = SUCCESS
			CLOSED = APPEND(CLOSED,[N])
			print("CLOSED=",CLOSED)
		else:
			CLOSED = APPEND(CLOSED,[N])
			print("CLOSED=",CLOSED)
			CHILD = MOVEGEN(N[0])
			print("CHILD=",CHILD)
			for val in CLOSED:
				if val in CHILD:
					CHILD.remove(val)
			for val in OPEN:
				if val in CHILD:
					CHILD.remove(val)
			OPEN = APPEND(CHILD,OPEN) #append movegen elements to OPEN
			print("Unsorted OPEN=",OPEN)
			SORT(OPEN)
			print("Sorted OPEN=",OPEN)
			
	Closed=CLOSED
	return State
	
result=BestFirstSearch() #call search algorithm
print(Closed,"\n\n")
print(result)

#

#Q3.best first search

from queue import PriorityQueue

# Filling adjacency matrix with empty arrays
vertices = 14
graph = [[] for i in range(vertices)]


# Function for adding edges to graph
def add_edge(x, y, cost):
    graph[x].append((y, cost))
    graph[y].append((x, cost))


# Function For Implementing Best First Search
# Gives output path having the lowest cost
def best_first_search(source, target, vertices):
    visited = [0] * vertices
    pq = PriorityQueue()
    pq.put((0, source))
    print("Path: ")
    while not pq.empty():
        u = pq.get()[1]
        # Displaying the path having the lowest cost
        print(u, end=" ")
        if u == target:
            break

        for v, c in graph[u]:
            if not visited[v]:
                visited[v] = True
                pq.put((c, v))
    print()


if __name__ == '__main__':
    # The nodes shown in above example(by alphabets) are
    # implemented using integers add_edge(x,y,cost);
    add_edge(0, 1, 1)
    add_edge(0, 2, 8)
    add_edge(1, 2, 12)
    add_edge(1, 4, 13)
    add_edge(2, 3, 6)
    add_edge(4, 3, 3)

    source = 0
    target = 2
    best_first_search(source, target, vertices)