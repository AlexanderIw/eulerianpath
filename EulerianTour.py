# Author: Lonique Alexander Udacity home work
# Find Eulerian Tour
# Write a function that takes in a graph
# represented as a list of tuples
# and return a list of nodes that
# you would follow on an Eulerian Tour
#
# For example, if the input graph was
# [(1, 2), (2, 3), (3, 1)]
# A possible Eulerian tour would be [1, 2, 3, 1]

def find_eulerian_tour(graph):
	length=len(graph); j=0
	origin= graph[0][0]		#The origin position
	b=origin 				#current position
	path=[];foundPath=False

	#copy the original array to reduce complexity
	tour= list(graph)
	
	#complexity of O(n^2)
	while j<length:

		origin=tour[j][0]

		#now we are going to search for the 
		# complexity of O(n)
		for i in range(0,length):
			if(connected(b, tour[i]) and tour[i] not in path):
				b=tour[i]
				path.append(tour[i])
				del tour[i]
				break

		#i am thinking breaking this up in to different taskes
		for t in tour:
			print "for in tour-->", b,"=",t
			if connected(b[1],t) and t not in path: 
				path.append(t)
				b=t
				foundPath=True
			else:
				foundPath=False
				print "not connected=",b, t
		
		if not foundPath: 
			backTrack(path.pop())		#path.pop() last elemented inserted 

		print "path=",path
		break
		#-------------------------------------------#
		#this is the winning condition
		if(j==length-1 and origin==b):
			for p in path:
				arrayFormPath.append(p[0])
			arrayFormPath.append(b)
			print "path==>",arrayFormPath
			return True
		#print "path update= ", path
		#print "----------------------------------------"
		j+=1
	#for s in supportArray: print "supportArray",s
	#print "path==>", path
	return tour

def connected(x,tup):
	if x==tup[0]: return True
	return False

def nextMove(t, b, origin, path):
	#t: tubple representing an edge
	#b: current possition
	#path: is a collection of all edges. the path from 1 node tot he next

	#if curSize==

	return True

def backTrack(t, b, path):
	return True

t1= [(1, 2), (2, 3), (3, 1)]
t2=[(0,1),(1,2),(2,0),(0,3),(3,4),(4,0)]
#harder example then t1 and t2
t3=[(1,0),(0,2),(2,1),(0,3),(3,4),(4,0)]
#even harder input. see if your program know what it's doing
t4=  [(0, 1), (1, 5), (1, 7), (4, 5),
(4, 8), (1, 6), (3, 7), (5, 9),
(2, 4), (0, 4), (2, 5), (3, 6), (8, 9)]
t5=[(1, 13), (1, 6), (6, 11), (3, 13),
(8, 13), (0, 6), (8, 9),(5, 9), (2, 6), (6, 10), (7, 9),
(1, 12), (4, 12), (5, 14), (0, 1),  (2, 3), (4, 11), (6, 9),
(7, 14),  (10, 13)]
t6=[(8, 16), (8, 18), (16, 17), (18, 19),
(3, 17), (13, 17), (5, 13),(3, 4), (0, 18), (3, 14), (11, 14),
(1, 8), (1, 9), (4, 12), (2, 19),(1, 10), (7, 9), (13, 15),
(6, 12), (0, 1), (2, 11), (3, 18), (5, 6), (7, 15), (8, 13), (10, 17)]
find_eulerian_tour(t3)