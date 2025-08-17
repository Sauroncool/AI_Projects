import numpy as np

class H:
    scaleV = 100
     # loop to keep changing

    def numbify(coords):
        i = 0
        flag = 0
        lat = ''
        lon = ''
        for ch in coords:
            if (ch == ','):
                flag += 1
            if (flag == 0):
                lon += coords[i]
            elif (ch != ','):
                lat += coords[i]
            i += 1
#        print(lat,lon)
        lati = float(lat)
        longi = float(lon)
        return ([lati, longi])






    def Euclid(p,q):
        # dx = (p[1] - q[1]) * 40000 * np.cos((p[0] + q[0]) * np.pi / 360) / 360
        # dy = (p[0] - p[1]) * 40000 / 360
        dy = (p[0] - q[0]) * 6371000 * np.pi / 180;
        dx = np.cos((p[0] + q[0]) / 2) * 6371000 * np.pi / 180 * (p[1] - q[1]);
        delx = dx
        dely = dy
        return np.sqrt((delx ** 2 + dely ** 2))



    def heuristic(n, g, lm1, lm2,avgV):
        W = H.scaleV/avgV  # scaling weight
        return (H.Euclid(n, lm1) + H.Euclid(lm1, lm2) + H.Euclid(lm2, g)) * W


