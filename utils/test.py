import requests
import urllib.parse

url = "https://raw.githubusercontent.com/pojiezhiyuanjun/freev2/master/1020.txt"
host = "http://127.0.0.1:25500"

url = urllib.parse.quote(url, safe='')
try:
  res = requests.get(f'{host}/sub?target=clash&url={url}&insert=false&emoji=true&list=true').text
  print(res)
except Exception as e:
  print(e)
