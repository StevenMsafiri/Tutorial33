import requests
LATITUDE = -6.792354
LONGITUDE = 39.208328

# response = requests.get(url="http://api.open-notify.org/iss-now.json")
# # if response.status_code == 404:
# #     raise Exception("Not Found, the resource does ot exist.")
# # elif response.status_code != 200:
# #     raise Exception("You are not allowed to access this resource.")
#
# data = response.json()
#
# longitude = data["iss_position"]["longitude"]
# latitude = data["iss_position"]["latitude"]
#
#
# iss_position = (longitude, latitude)
# print(iss_position)

parameter = {
    "lat": LATITUDE,
    "lng": LONGITUDE,
}

response = requests.get(url=f"https://api.sunrise-sunset.org/json", params=parameter)
data = response.json()

print(data)
