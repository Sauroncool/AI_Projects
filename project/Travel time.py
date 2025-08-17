import requests

def travel_time(slat,slon,elat,elon):

    start_latitude=slat
    end_latitude=elat
    start_longitude=slon
    end_longitude=elon

    # Replace with your API endpoint and authorization token
    api_url = "https://api.tomtom.com/routing/1/calculateRoute/"
    auth_token = "LBkwGiXhNysmO1FVdJneKAzw7M2bhGeB"

    two_points = str(start_latitude) + "%2C" + str(start_longitude) + ":" + str(end_latitude) + "%2C" + str(
        end_longitude)

    # make API call to get data
    route_data = requests.get(api_url + two_points + str("/json?traffic=true&key=") + auth_token)
    route_json = route_data.json()

    # print(route_json)  # printing json data

    travel_time = route_json['routes'][0]['summary']['travelTimeInSeconds']
    traffic_delay = route_json['routes'][0]['summary']['trafficDelayInSeconds']
    travel_length = route_json['routes'][0]['summary']['lengthInMeters']

    # print("Traffic Distance=", travel_length / 1000, " km")
    # print("Travel Time=", travel_time / 3600, " hours")
    # print("Traffic Delay=", traffic_delay / 60, " minutes")
    # print("Speed", (travel_length / 1000) / (travel_time / 3600), " km/h")
    return (travel_length / 1000) / (travel_time / 3600)

# start_latitude = 8.62604
# start_longitude = 77.03460  # Near IIST library location
#
# end_latitude = 8.51165
# end_longitude = 76.96699
#
# print(travel_time(start_latitude,start_longitude,end_latitude,end_longitude))