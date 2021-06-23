import requests

from datetime import datetime

outfile=open('data.txt','w')
api_key = 'd3740df89788149aa29ee05de6c79a64'
location = input("Enter the city name: ")

complete_api_link = "https://api.openweathermap.org/data/2.5/weather?q="+location+"&appid="+api_key
api_link = requests.get(complete_api_link)
api_data = api_link.json()


temp_city = ((api_data['main']['temp']) - 273.15)
weather_desc = api_data['weather'][0]['description']
hmdt = api_data['main']['humidity']
wind_spd = api_data['wind']['speed']
date_time = datetime.now().strftime("%d %b %Y | %I:%M:%S %p")
date_time = datetime.now().strftime("%d %b %Y | %I:%M:%S %p")

outfile.write("-------------------------------------------------------------"+"\n")
outfile.write("Weather Stats for - {}  || {}".format(location.upper(), date_time)+"\n")
outfile.write("-------------------------------------------------------------"+"\n")

outfile.write("Current temperature is: {:.2f} deg C".format(temp_city)+"\n")
outfile.write("Current weather desc  : "+weather_desc+"\n")
outfile.write("Current Humidity      :"+str(hmdt)+"\n")
outfile.write("Current wind speed    :"+ str(wind_spd) +'kmph'+"\n")
