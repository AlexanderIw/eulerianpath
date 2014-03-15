# Author: Lonique Alexander Udacity home work
# last updated: 03/14/2014

def find_eulerian_tour(graph):
	length=len(graph);
	path=[]; tour=[]; lib={}

	curNode=graph[0][0]
	while True:
		curNode=nextMove(curNode, lib,path,graph,length)
		if curNode==None:

			if isTourCompleted(path,length):
				return udacityFormat(path)
			else:
				curNode=path[-1][1]
				curNode=backTrack(curNode,lib, path)

				if curNode==None: break		# No solution
				continue

def connected(n,t): 
	return (n==t[1] or n==t[0])

def nextMove(b, lib, path, tour,length):
	ary=[]; lib[b]=[]
	for i in range(0,length):
		if(connected(b, tour[i]) and isInPath(tour[i],path)):
			y=tour[i][0] if tour[i][1]==b else tour[i][1]
			ary.append((b,y))
	
	if len(ary)<=0: return None
	
	while len(ary)>1: lib[b].append(ary.pop())

	path.append(ary.pop())
	return path[-1][1]

def isInPath(tour, path):
	x= (tour[1],tour[0])
	if tour not in path and x not in path:
		return True
	return False

def isTourCompleted(path,length):
	if len(path)!=length: return False		#All edges must be visited
	if path[0][0]!=path[-1][1]:return False #check start node == last node
	return True							#if pass these two condition then it eulerian circuit

def backTrack(b,lib, path):
	while not len(lib[b]):
		path.pop()
		b=path[-1][1]
		if len(lib)==0: return 		

	path.append(lib[b].pop())
	return path[-1][1]

def udacityFormat(path):
	newPath=[]
	for t in path:
		newPath.append(t[0])
	newPath.append(path[-1][1])
	return newPath

t4=  [(0, 1), (1, 5), (1, 7), (4, 5),
(4, 8), (1, 6), (3, 7), (5, 9),
(2, 4), (0, 4), (2, 5), (3, 6), (8, 9)]
print find_eulerian_tour(t4)	