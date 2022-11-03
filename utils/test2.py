import requests

local = '0.0.0.0:3333'

response = requests.get(f'{local}/get-base64?content=https://raw.githubusercontent.com/MOnday9907/v2ray/main/v2ray.txt').text

print(response)
