from route_adv import route as r

class mape:
	def draw(start, end):
		#List of all coordinates
		keylst=[]
		#2D List of all routes
		routes = r.intersections(start,goal)
		for i in range(len(routes)):
		#	print(routes[i].keys())
			keylst.append(list(routes[i].keys()))
			print(i+1," iteration")
		#	for key in routes[i]:
		#		print(routes[i][key])
				#all the distances here
		#print(keylst)

		#dictionary for final values
		graph = {}

		graph[keylst[0][0]]=[]
		current = keylst[0][0]
		i=0
		j=0
		sum=0
		for i in range(len(keylst)):
			for j in range(len(keylst[i])):
				print(keylst[i][j])
				sum+=routes[i][keylst[i][j]]
				if j==0:
					continue
				c=0
				#rejoin
				for k in range(len(keylst)):
					for l in range(len(keylst[k])):
						if (k==i) or l==0:
							continue
						if keylst[i][j] == keylst[k][l] and not keylst[i][j-1] == keylst[k][l-1] :
							graph[current].append([keylst[i][j],sum])
							current = keylst[i][j]
							sum=0
				#split
				for k in range(len(keylst)):
					for l in range(len(keylst[k])):
						if (k==i) or l==(len(keylst[i])-1):
							econtinue
						if keylst[i][j] == keylst[k][l] and not keylst[i][j+1] == keylst[k][l+1] :
							current = keylst[i][j]
							graph[current].append([keylst[i][j+1],sum])
							sum = 0
		return(graph)

print(mape.draw())
