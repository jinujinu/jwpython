import sys
import io
import requests
import json


sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

key ="51534177436a696e35317958444266"

print('http://openapi.seoul.go.kr:8080/{0}/json/RealtimeCityAir/1/99'.format(key))

re = requests.get('http://openapi.seoul.go.kr:8088/{0}/json/RealtimeCityAir/1/99'.format(key))
rjson = re.json()

r2json = json.dump(rjson)

print(r2json)
print(type(re))
print(type(rjson))
print(type(r2json))

#
# print("test")
# print(rjson)
# print(re.status_code)

# printf(re)
