import requests
import json
x = input("Enter city name: ")
url = f"https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline/{x}?unitGroup=us&key=2PDECTVSRRXFHPLRSX5WXEQ9G&contentType=json"

r = requests.get(url)
dic = r.text
py_dict = json.loads(dic)
weather = py_dict["currentConditions"]["temp"]

print("The temperature is ",(weather-32)*5/9,"c")


