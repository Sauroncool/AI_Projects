import requests, json

class currloc:
    def loc():
        x = requests.get('http://localhost:8000/loc.json')
        data = list(x.json().keys())[0]
        us=0;
        c=0
        lat=''
        lon=''
        for ele in data:
            if(ord(ele)<=57 and ord(ele)>=48):
                if(c==0):
                    lat+=ele
                elif(c==1):
                    lon+=ele
            elif(ele=='_'):
                us+=1
                if(us==1 or us==3):
                    ele=' '
                    if(us==3):
                        c=1
                    if (c == 0):
                        lat += ele
                    elif (c == 1):
                        lon += ele
                elif(us==2 or us==4):
                    ele='.'
                    if(c==0):
                        lat+=ele
                    elif(c==1):
                        lon+=ele
        coords=''
        coords=coords+lon[1:]+','+lat[1:]
        print(coords)
        return coords
print(currloc.loc())
