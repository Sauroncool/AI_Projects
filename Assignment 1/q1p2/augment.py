import numpy as np

class graph:
	Graph = {} #This dictionary stores the problem as a tree

	H = {} #This dictionary stores heuristics of each node

	start = '(1,11)' #Define the start node

	goal = '(15,11)' #Define the goal node

	#Define a distance function to calculate euclidean distance to the goal
	def dist(i,j,):
		return np.sqrt((int(graph.goal[graph.goal.rindex('(')+1:graph.goal.rindex(',')-1:])-i)**2+(int(graph.goal[graph.goal.rindex(',')+1:graph.goal.rindex(')')-1:])-j)**2)

	def generate():
		#Formulate the maze here
		global maze
		maze=[[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1],
           [1, 0, 0, 0, 1, 0, 1, 0, 0, 1, 0, 0, 0, 1, 1],
           [1, 0, 1, 0, 1, 0, 1, 0, 1, 1, 0, 1, 1, 0, 1],
           [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 0, 1, 0, 0, 1],
           [1, 0, 1, 0, 1, 1, 1, 0, 1, 0, 1, 0, 0, 0, 1],
           [1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 1],
           [1, 0, 1, 1, 0, 1, 0, 1, 1, 0, 1, 0, 1, 0, 1],
           [1, 0, 0, 0, 0, 1, 0, 0, 1, 0, 1, 0, 1, 0, 1],
           [1, 1, 1, 1, 0, 1, 0, 1, 1, 0, 1, 0, 1, 0, 1],
           [1, 0, 0, 1, 0, 1, 0, 1, 0, 0, 1, 0, 0, 0, 1],
           [1, 0, 1, 1, 0, 1, 0, 1, 1, 0, 1, 0, 1, 0, 1],
           [1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 1],
           [1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1],
           [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
           [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1]]
		for i in range(len(maze)): #Print the maze
			for j in range(len(maze[i])):
				print(str(maze[i][j])+" ", end="")
			print("")

		for i in range(len(maze)):
			for j in range(len(maze[i])):
				k=i+1
				l=j+1
				graph.H['('+str(k)+','+str(l)+')']=graph.dist(i,j) #Add heuristics to each node
				graph.Graph['('+str(k)+','+str(l)+')']=[]
				#Add the neighbours to each key in the {Graph} dictionary
				if i>0:
					if maze[i-1][j]==0:
						graph.Graph['('+str(k)+','+str(l)+')'].append(['('+str(k-1)+','+str(l)+')',1])
				if i<(len(maze)-1):
					if maze[i+1][j]==0:
						graph.Graph['('+str(k)+','+str(l)+')'].append(['('+str(k+1)+','+str(l)+')',1])
				if j>0:
					if maze[i][j-1]==0:
						graph.Graph['('+str(k)+','+str(l)+')'].append(['('+str(k)+','+str(l-1)+')',1])
				if j<(len(maze[i])-1):
					if maze[i][j+1]==0:
						graph.Graph['('+str(k)+','+str(l)+')'].append(['('+str(k)+','+str(l+1)+')',1])

	def output(path):
		print('Path will look like this')
		for i in range(len(maze)):
			for j in range(len(maze[i])):
				if '('+str(i+1)+','+str(j+1)+')' in path:
					print('*' + " ", end="")
				else:
					print('|' + " ", end="")
			print("")

	def heur(n):
		return graph.H[n]
