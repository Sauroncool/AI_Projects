import requests, json

class route:
    def intersections(start, end):
        response = requests.get("https://apis.mapmyindia.com/advancedmaps/v1/60d3c56b5a491f80391ddb3b59ac20e7/route_adv/driving/"+start+";"+end+"?alternatives=3&steps=true")
        #Obtaining the results from MapMyIndia API​
        result=response.json()
        #Converting the results to a dictionary​
        route_int = []

        for i in range(len(result['routes'])):
            tempdict = {}
            for j in range(len(result['routes'][i]['legs'][0]['steps'])):
                loc = str(result['routes'][i]['legs'][0]['steps'][j]['maneuver']['location'][0]) + ',' + str(result['routes'][i]['legs'][0]['steps'][j]['maneuver']['location'][1]) #Location of the current intersection in the form of '<longitude>,<latitude>'​
                tempdict[loc] = result['routes'][i]['legs'][0]['steps'][j]['distance']
            route_int.append(tempdict)
        # print(route_int)
        return route_int

# route.intersections()
