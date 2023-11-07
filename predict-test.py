
import requests


url = 'http://localhost:9696/predict'

customer_id = 'xyz-123'
flight ={
    'id':100,
    'airline' : 'us',
    'flight' : 'sdfsdf',
    'airportfrom' : 'bwi',
    'airportto' : 'clt',
    'dayofweek' : 4,
    'time' : 325,
    'length' : 83
}


response = requests.post(url, json=flight).json()
print(response)


if response['delay'] == True:
    print(f'sending alert email to {customer_id}')
else:
    print(f'not sending alert email to to {customer_id}')


