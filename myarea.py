import requests
MY_LAT = -27.36679

MY_LONG = -70.3314

parameters = {
    "lat": MY_LAT,
    "lng":  MY_LONG,
    "formatted": 0
}

responses = requests.get(url="https://api.sunrise-sunset.org/json", params=parameters, verify= False)

responses.raise_for_status()
myData = responses.json()


sunRiseMyLong_hour = int(myData["results"]['sunrise'].split("T")[1].split(":")[0])
sunSetMyLat_hour = int(myData["results"]["sunset"].split("T")[1].split(":")[0])



