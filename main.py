import requests
import json
import sqlite3

#ვუკავშირდებით ამინდის api-ს
city = input("შეიყვანეთ სასურველი ქალაქი: ")
api_key = '1d849b5d5e5e96d7c173de74ee2f6028'
resp = requests.get(f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric")

print(" Status Code: ", resp.status_code, '\n', "Header", resp.headers)


#json ფაილში გადატანა
resour = json.loads(resp.text)
resp_json_structured = json.dumps(resour, indent=4)
with open ("amindi.json", "w") as file:
    json.dump(resour, file, indent=4)


#ინფორმაციის კონსოლში გამოტანა
k = resour['main']
temp = k['temp']
tenianoba = k['humidity']
print(" ტემპერატურა", temp, '\n', "ტენიანობა", tenianoba)


#ინფორმაცია მონაცემთა ბაზაში შენახვა
conn = sqlite3.connect("database_weather.sqlite")
cursor = conn.cursor()
# cursor.execute('''CREATE TABLE amindi
#                 (id INTEGER PRIMARY KEY AUTOINCREMENT,
#                  CityName VARCHAR(50),
#                  Temp VARCHAR(50),
#                  Humidity VARCHAR(50));''')

cursor.execute("INSERT INTO amindi (CityName, Temp, Humidity) VALUES (?, ?, ?)", (city, temp, tenianoba))
conn.commit()