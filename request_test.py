import requests
import json

print('Hello World')

def get_valutes_list():
    url = 'https://www.cbr-xml-daily.ru/daily_json.js'
    response = requests.get(url)
    data = json.loads(response.text)
    valutes = list(data['Valute'].values())
    return valutes

valutes = get_valutes_list()
print(type(valutes))
for i in valutes:
    for j in i.values():
        print (j,'__',end='')
    print()
