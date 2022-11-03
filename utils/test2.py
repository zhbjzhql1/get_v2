import requests

local1 = 'http://127.0.0.1:3333'
local2 = 'http://0.0.0.0:3333'

try:
  response1 = requests.get(f'{local1}/get-base64?content=https://raw.githubusercontent.com/MOnday9907/v2ray/main/v2ray.txt').text
except:
  pass
try:
  response2 = requests.get(f'{local2}/get-base64?content=https://raw.githubusercontent.com/MOnday9907/v2ray/main/v2ray.txt').text
except: 
  pass

print(response1)
print('-----------------------------')
print(response2)
