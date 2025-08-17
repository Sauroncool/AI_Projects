import requests
import matplotlib.pyplot as plt
import imageio.v2 as imageio

# Replace with your API endpoint and authorization token
api_url = "https://api.tomtom.com/routing/1/calculateRoute/"
auth_token = "LBkwGiXhNysmO1FVdJneKAzw7M2bhGeB"

start_latitude = 8.62604
start_longitude = 77.03460  # Near IIST library location

end_latitude = 8.51165
end_longitude = 76.96699

two_points = str(start_latitude) + "%2C" + str(start_longitude) + ":" + str(end_latitude) + "%2C" + str(end_longitude)

# make API call to get data
route_data = requests.get(api_url + two_points + str("/json?traffic=true&key=") + auth_token)

route_json = route_data.json()

print(route_json)  # printing json data

# Initialize our 2 arrays that will contain all the points
lat = []
long = []
# Iterate through all the points and add the lat and long to the correct array
for point in route_json['routes'][0]['legs'][0]['points']:
    lat.append(point['latitude'])
    long.append(point['longitude'])

# Convert the points to floats
lat = [float(x) for x in lat]
long = [float(x) for x in long]

mid_lat = (start_latitude + end_latitude) / 2
mid_lon = (start_longitude + end_longitude) / 2

center_pos = str(mid_lon) + "," + str(mid_lat)
image = requests.get(
    "https://api.tomtom.com/map/1/staticimage?key=" + auth_token + "&zoom=10&center=" + center_pos + "&format=png&layer=basic&style=main&view=IN&language=en-GB")

# Read the image from the request
im = imageio.imread(image.content)

# Create the figure
plt.figure()
# Show the image
plt.imshow(im, extent=(
    round(max(start_longitude, end_longitude), 1) + 0.1, round(min(start_longitude, end_longitude), 1) - 0.1,
    round(max(start_latitude, end_latitude), 1) + 0.1, round(min(start_latitude, end_latitude), 1) - 0.1))
plt.scatter(long, lat)
plt.show()
