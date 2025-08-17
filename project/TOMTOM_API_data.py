import requests

# Replace with your API endpoint and authorization token
api_url = "https://api.tomtom.com/search/2/categorySearch"
auth_token = "LBkwGiXhNysmO1FVdJneKAzw7M2bhGeB"


def Hospital(lat,lon):
    country = "IN"

    search = "Hospital"  # search item

    position = "&lat=" + str(lat) + "&lon=" + str(lon) + "&key="
    country_set = "?countrySet=" + country
    search_key = "/" + search + ".json"

    # make API call to get data
    traffic_data = requests.get(api_url + search_key + country_set + position + auth_token)
    traffic_json = traffic_data.json()
    # print(traffic_json)  # printing json data

    # print('\n\n')
    for result in traffic_json['results']:
        # print('Name:', result['poi']['name'])
        # print('Address:', result['address']['freeformAddress'])
        # print('Position:', result['entryPoints'][0]['position']['lat'], ',',
        #       result['entryPoints'][0]['position']['lon'])
        # print('Distance:', str(round(result['dist']) / 1000), ' km', '\n\n')
        return result['entryPoints'][0]['position']['lat'],result['entryPoints'][0]['position']['lon']
        # break

# # Defining position
# latitude = 8.62604
# longitude = 77.03460  # Near IIST library location
# Hospital(latitude,longitude)
# print(Hospital(latitude,longitude))