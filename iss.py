import requests
responseiss = requests.get("http://api.open-notify.org/iss-now.json")

issdata = responseiss.json()


def issposition(data):
    longitude = data["iss_position"]["longitude"]
    latitude = data["iss_position"]["latitude"]
    print(longitude, latitude)



issdata = responseiss.json()


iss_data = issposition(issdata)