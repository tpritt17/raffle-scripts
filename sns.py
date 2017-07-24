import requests
import time

print(time.strftime("%H:%M:%S") + " / SNS raffle script for Mars Yard 2.0 by @jamzigod\n")

def raffle(limit):
 
 sizes = ["US 6','US 7', 'US 8', 'US 8.5', 'US 9', 'US 9.5', 'US 10' ,'US 10.5' ,'US 11' ,'US 11.5' ,'US 12', 'US 13"]

 s = requests.session()

 url = "https://sneakersnstuff.typeform.com/app/form/submit/Hathk3"

 headers = {

             'User-Agent':
             'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36'

            }

 data = {

        'form[language]': 'en',
        'form[yes-no:warE3SilldbG]': '1',
        'form[email:Fi1mS3bZn3VF]': 'washed@gmail.com', #CHANGE EMAIL
        'form[list:56641463][choices]': sizes ,
        'form[list:56641463][other]': '',
        'form[textfield:IIdtgeMwp8Gp]':'Jamzi', #FIRST NAME
        'form[textfield:bHSS1rapvhha]':'God', #SECOND NAME
        'form[textfield:EKZm78mYLBbE]':'46 street', #HOUSE NO, STREETNAME
        'form[textfield:Boa0BNN75u6R]':'London', #CITY
        'form[textfield:MQfwQiem4TEw]':'XXX XXX', #POSTCODE
        'form[textfield:n3yXjbpstFmJ]':'none', #STATE IF EU 'NONE'
        'form[textfield:u9og65Z22NNB]':'United Kingdom', #COUNTRY
        'form[terms:QS4P6gmSVp8s]':'1',
        'form[landed_at]':'1500906325',
        'form[token]':'7c31acc80cf05c08eb28e5fc263ee628$2y$11$e2dJZC0zIXZQK1pxbSZbL.NJ1u84MZYcsL6lUR1WKI2mbDgYfcium'

 }

 res = s.post(url, data=data, headers=headers)

 if "success" in (res.text):
    print(time.strftime("%H:%M:%S") + " / Succesfully entered SNS raffle for Mars Yard 2.0!")

 else:
    print(time.strftime("%H:%M:%S") +  " / Couldnt enter raffle!")
    exit()

while True:
        raffle(10000)
