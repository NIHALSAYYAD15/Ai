#Program for breadth first search

tree={
    'A':['B','C','D'],
    'B':['E'],
    'C':['F','G'],
    'D':['H'],
    'E':['I','J'],
    'F':[],
    'G':[],
    'H':['K'],
    'I':[],
    'J':[],
    'K':[]
}

#create visited list and queue list
visited=[]
queue=[]

def bfs(visited,queue,node):
    visited.append(node)
    queue.append(node)

    while queue:
        m=queue.pop(0)
        print(m,end=" ")

        for neighbour in tree[m]:
            if neighbour not in visited:
                visited.append(neighbour)
                queue.append(neighbour)

#main
print("Following is breadth first Search :\n")
bfs(visited,queue,"A")

#

#Q2. Breadth-first Search

graph = {
  '5' : ['3','7'],
  '3' : ['2', '4'],
  '7' : ['8'],
  '2' : [],
  '4' : ['8'],
  '8' : []
}

visited = [] # List for visited nodes.
queue = []     #Initialize a queue

def bfs(visited, graph, node): #function for BFS
  visited.append(node)
  queue.append(node)

  while queue:          # Creating loop to visit each node
    m = queue.pop(0)
    print (m, end = " ")

    for neighbour in graph[m]:
      if neighbour not in visited:
        visited.append(neighbour)
        queue.append(neighbour)

# Driver Code
print("Following is the Breadth-First Search")
bfs(visited, graph, '5')    # function calling
