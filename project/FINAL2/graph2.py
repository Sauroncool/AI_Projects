from route_adv import route as r
from heurAIR import H
class mape:
	def draw(start, end):
		#List of all coordinates
		keylst=[]
		nkeylst=[]
		#2D List of all routes
		Route = r.intersections(start,end)
		routes = Route.copy()
#		print(routes)
		graph = {}
#		print(routes)
		count = 0
		for i in range(len(routes)):
		#	print(routes[i].keys())
			nkeylst.append(list(routes[i].keys()))
			keylst.append(list(routes[i].keys()))
			for j in range(len(routes[i].keys())):
				lati = round(H.numbify(keylst[i][j])[0],4)
				longi = round(H.numbify(keylst[i][j])[1],4)
				nkeylst[i][j] = str(count)
				count+=1
#				nkeylst[i][j] = str(longi)+','+str(lati)
				graph[nkeylst[i][j]] = []


		current = keylst[0][0]
		nstart = str(round(H.numbify(start)[1],4))+','+str(round(H.numbify(start)[0],4))
#		graph[nstart] = []
		nstart = '0'
		End = ''
		c=0
		for i in range(len(nkeylst)):
			for j in range(len(nkeylst[i])-1):
				if j == 0:
					graph[nstart].append((nkeylst[i][j+1],routes[i][keylst[i][j]]))
					c+=1
					continue
				c+=1
				
				if j == len(nkeylst[i])-2:
					End = str(c)
					graph[nkeylst[i][j]]=[(End,routes[i][keylst[i][j]])]
					
#					End = str(round(H.numbify(end)[1],4))+','+str(round(H.numbify(end)[0],4))
					continue
#					print(keylst[i][j+1])
				graph[nkeylst[i][j]].append((nkeylst[i][j+1],routes[i][keylst[i][j]]))
		
#		graph[start] = graph[current]
#		graph[keylst[len(keylst)-1][c-2]] = (end,routes[len(routes[i])-1][keylst[len(keylst)-1][c-2]])
#		print('end = ',graph[keylst[len(keylst)-1][c-1]])
#		print('end = ',End)
#		print(graph)
		return(graph,End,nstart,keylst,nkeylst)

print(mape.draw("77.2303,28.6505", "77.210,28.5672"))
#mape.draw("77.2303,28.6505", "77.210,28.5672")
