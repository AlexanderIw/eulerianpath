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
	length=len(graph); path=[]
	size= len(graph)+1; j=0
	b= graph[0][0]; prev=graph[0][0]			
	explore=[]; 
	supportArray=[None]*length

	size=2

	while j<size:
		for i in range(0,length):
			if(equalEdge(b, graph[i])):
				explore.append(graph[i])

		print "explore",explore
		
		print "before b=", b
		prev=b
		b=explore.pop()				#pop one of the option of the stack
		if explore:
			print "how man time i make it hear"
			supportArray[j]=explore		#it's equal to the remainder at position j
		explore=[]

		print "before inserted in pathb= ",b
		if b not in path: path.append(b)

		b=b[1] if b[0]==prev else b[0]


		print "after b=", b

		j+=1
	#for s in supportArray: print "supportArray",s
	print "path==>", path
	return path

def equalEdge(x,tup):
	if x==tup[0]: return True

t1= [(1, 2), (2, 3), (3, 1)]
t3=[(1,0),(0,2),(2,1),(0,3),(3,4),(4,0)]
t2=[(1,0),(0,3),(3,4),(4,0),(0,2),(2,1)]

find_eulerian_tour(t2)