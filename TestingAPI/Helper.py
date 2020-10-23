import requests

response = requests.get('http://dummy.restapiexample.com/api/v1/employees', headers={"User-Agent": "XY"})
#print(response.json())

assert 2 + 3 == 5