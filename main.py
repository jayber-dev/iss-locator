import requests
import json
import smtplib
MY_LOCATION = [0, 174.4977]
EMAIL = "jayber1@yahoo.com"
PASSWORD = "yvfngtkvredjkygx"
print(MY_LOCATION[1] + 5)
work = True
while work:
    web_data = requests.get(url="http://api.open-notify.org/iss-now.json")
    x = web_data.json()
    data_latitude = float((x["iss_position"]["latitude"]))
    data_longitude = float((x["iss_position"]["longitude"]))

    iss_data = [data_latitude, data_longitude]

    if MY_LOCATION[0] - iss_data[0] <= 5 and MY_LOCATION[1] - iss_data[1] <= 5:
        with smtplib.SMTP("smtp.mail.yahoo.com") as send:
            send.starttls()
            send.login(user=EMAIL, password=PASSWORD)
            send.sendmail(from_addr=EMAIL, to_addrs="jayber1@gmail.com", msg="subject: iss space station \n\n "
                                                                             "hey look up the iss above you")
            print("mail sent")
        work = False
    print(iss_data)
