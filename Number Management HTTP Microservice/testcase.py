import requests
import json
url = "http://localhost:8008/numbers?url=http://20.244.56.144/numbers/primes&url-http://abc.com/fibo "

response = requests.get(url)

if response.status_code == 200:
  numbers = json.loads(response.content)["numbers"]
  print(numbers)
else:
  print("Error: {}".format(response.status_code))
