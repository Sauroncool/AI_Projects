import time
from heurAIR import H
from graph2 import mape
from Hospital_loc import *
from travel_speed import *
from loc import currloc
from search import find

# Final
nowloc = [0, 0]
goalloc = [0.01, 0]
while (H.Euclid(nowloc, goalloc) >= 50):
    cloc = currloc.loc()

    latitude = H.numbify(cloc)[0];
    longitude = H.numbify(cloc)[1];
    c = 0
    # for ch in cloc:
    #     if ch == ',':
    #         continue
    #     if c == 0:
    #         longitude+=ch
    #     else:
    #         latitude+=ch
    # print(Hospital(latitude, longitude))
    Hospital(latitude, longitude)  # It will give location in format of latitude and longitude in 'float' datatype

    lat, lon = Hospital(latitude, longitude)
    # lat = 8.504695
    # lon = 76.97164
    end = str(lon) + ',' + str(lat)

    # travel_speed(slat,slon,lat,lon) # Add all parameters in float format

    #    print(mape.draw(cloc, end))

    coordsNow = cloc
    coordsGoal = end
    coordsStart = cloc
    coordLandmark1 = ''
    coordLandmark2 = ''
    coordsNext1 = ''
    coordsNext2 = ''
    avgS = ''
    nowloc = H.numbify(coordsNow)
    goalloc = H.numbify(coordsGoal)
    startloc = H.numbify(coordsStart)
    lm1loc = nowloc
    lm2loc = goalloc
    # nextloc1 = H.numbify(coordsNext1)
    # nextloc2 = H.numbify(coordsNext2)  # returns coords of the nodes of start, goal, current and landmarks in tuple form
    print("Answer=", find.aStar(coordsNow, coordsGoal))
    time.sleep(10)
