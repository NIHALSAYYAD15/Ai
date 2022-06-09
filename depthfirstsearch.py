#Program for depth first search


#generate tree using dictionary 
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

#create a set for storing visited node
visited=set()

#define a function dfs 

def dfs(tree,visited,node):
    if node not in visited:                     #check if node is visited or not
        print(node)
        visited.add(node)                       #add node to visited
        for neighbour in tree[node]:            #traverse neighbour 
            dfs(tree,visited,neighbour)         #call dfs recursively


#main
print("Folllowing is depth first search :\n")
dfs(tree,visited,'A')

#

# Q1.Depth First Search

# Using a Python dictionary to act as an adjacency list
graph = {
  '5' : ['3','7'],
  '3' : ['2', '4'],
  '7' : ['8'],
  '2' : [],
  '4' : ['8'],
  '8' : []
}

visited = set() # Set to keep track of visited nodes of graph.

def dfs(visited, graph, node):  #function for dfs
    if node not in visited:
        print (node)
        visited.add(node)
        for neighbour in graph[node]:
            dfs(visited, graph, neighbour)

# Driver Code
print("Following is the Depth-First Search")
dfs(visited, graph, '5')
