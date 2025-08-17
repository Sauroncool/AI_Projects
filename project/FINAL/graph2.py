from route_adv import route as r

class mape:
	def draw(start, end):
		#List of all coordinates
		keylst=[]
		#2D List of all routes
		routes = r.intersections(start,end)
		graph = {}
#		print(routes)
		for i in range(len(routes)):
		#	print(routes[i].keys())
			keylst.append(list(routes[i].keys()))
			for j in range(len(routes[i].keys())):
				graph[keylst[i][j]] = []

		

		current = keylst[0][0]
		c=0
		for i in range(len(keylst)):
			for j in range(len(keylst[i])-1):
				c+=1
				graph[keylst[i][j]].append((keylst[i][j+1],routes[i][keylst[i][j]]))
				
		
		graph[start] = graph[current]
		# graph[keylst[len(keylst)-1][c-2]] = (end,routes[len(routes[i])-1][keylst[len(keylst)-1][c-2]])
		
		return(graph)

# print(mape.draw("77.2303,28.6505", "77.210,28.5672"))
