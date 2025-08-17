from route_adv import route as r

class mape:
	def draw(start, end):
		#List of all coordinates
		keylst=[]
		#2D List of all routes
		routes = r.intersections()
		graph = {}
#		print(routes)
		for i in range(len(routes)):
		#	print(routes[i].keys())
			keylst.append(list(routes[i].keys()))

		
		graph[keylst[0][0]]=[]
		current = keylst[0][0]
		sum = 0
		for i in range(len(keylst)):
			for j in range(len(keylst[i])-1):
				split = 0
				sum+=routes[i][keylst[i][j]]
				for k in range(len(keylst)):
					#rejoin
					for l in range(len(keylst[i])):
						if l==0 or j==0:
							continue
						if keylst[i][j] == keylst[k][l] and not keylst[i][j-1] == keylst[k][l-1] :
							rejoin+=1
							graph[current].append([keylst[i][j],sum])
							sum = 0
						
					#split
					if k<=i:
						continue
					for l in range(len(keylst[i])):
						if l==len(keylst[i])-1 or j==len(keylst[i])-1:
							continue
						if keylst[i][j] == keylst[k][l] and not keylst[i][j+1] == keylst[k][l+1] :
							graph[current].append([keylst[i][j],sum])
							split+=1
							sum = 0
				
				if not split == 0:
					graph[keylst[i][j]].append([keylst[i][j+1],routes[i][keylst[i][j]]])
					current = keylst[i][j+1]
		
		
		
		
		return(graph)

print(mape.draw("77.2303,28.6505", "77.210,28.5672"))
