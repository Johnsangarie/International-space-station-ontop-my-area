import requests
responseiss = requests.get("http://api.open-notify.org/iss-now.json")

issdata = responseiss.json()


def issposition(data):
    long_lat_iss = []
    longitude = data["iss_position"]["longitude"]
    latitude = data["iss_position"]["latitude"]
    long_lat_iss.append(longitude)
    long_lat_iss.append(latitude)
    print(long_lat_iss)





issdata = responseiss.json()


iss_data = issposition(issdata)

