

'''Depth First Search uses STACK AND RECURSION
'''
#import defaultdict
from collections import defaultdict
def dfs(graph,start,visited,path):
    path.append(start)
    visited[start]=True
    for neighbour in graph[start]:
       #type ur code here
       if not visited[neighbour]:
        dfs(graph,neighbour,visited,path)
    return path
graph=defaultdict(list)
n,e=map(int,input().split())
for i in range(e):
   #type ur code here
    u,v=input().split()
    graph[u].append(v)
    graph[v].append(u)
#print(graph)
start='A'
visited=defaultdict(bool)
 #type ur code here
path=[]
traversedpath=dfs(graph,start,visited,path)
print(traversedpath)
