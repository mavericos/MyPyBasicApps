import credentials
import requests
import schedule
import time

def send_message():
    resp = requests.post("https://textbelt.com/text",{
        "phone" : mobile_number,
        "message" : "Hey, Good morning",
        "Key" : "textbelt"
    })
    print(resp.json())

# schedule.every().day.at("06:00").do(send_message)
schedule.every(5).seconds.do(send_message)

while True:
    schedule.run_pending()
    time.sleep(1)