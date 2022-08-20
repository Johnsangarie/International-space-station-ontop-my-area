import smtplib

from iss import iss_data

from myarea import MY_LAT, MY_LONG, sunRiseMyLong_hour, sunSetMyLat_hour

from datetime import datetime

import time

import smtpd

My_EMAIL = "michealbundor9@gmail.com"
MY_PASSWORD = "LYDIAsesay123"


def iss_overhead():
    iss_lat = iss_data[1]
    iss_long_position = iss_data[0]

    # check if my position is within +5  or -5 from that of the iss position.
    if MY_LAT - 5 <= iss_lat <= MY_LAT + 5 and MY_LONG - 5 <= iss_long_position <= iss_long_position + 5:
        return True


currentTimeHour = datetime.now().hour


def is_night(sunset_hour, sunrise_hour):
    if currentTimeHour >= sunset_hour or currentTimeHour <= sunrise_hour:
        return True


sunRiseMyLong_hour
sunSetMyLat_hour

is_night(sunSetMyLat_hour, sunRiseMyLong_hour)




while True:
    time.sleep(60)
    if iss_overhead() and is_night(sunSetMyLat_hour, sunRiseMyLong_hour):
        connection = smtplib.SMTP("smtp.gmail.com")
        connection.starttls()
        connection.login(My_EMAIL, MY_PASSWORD)
        connection.sendmail(
            from_addr=My_EMAIL,
            to_addrs=My_EMAIL,
            msg="subject: look up\n\n The iss above you in the sky"
        )
