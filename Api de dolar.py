import requests
import json 

request = requests.get('https://s3.amazonaws.com/dolartoday/data.json')
charge = json.loads(request.text)
usd = charge['USD']
dolar = usd['transferencia']

print("El precio de dolar hoy es:","$"+str(dolar))