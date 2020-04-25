import requests
from bs4 import BeautifulSoup
import pandas as pd

url = requests.get("http://forecast.weather.gov/MapClick.php?lat=37.7772&lon=-122.4168")

soup = BeautifulSoup(url.content, 'html.parser')

seven_days = soup.find(id="seven-day-forecast")

forecast_items = seven_days.find_all(class_= "tombstone-container")
# print(forecast_items)

seven_days_list = seven_days.select(".tombstone-container .period-name" )   #gettinf all periods for the site. gives list pf objects
periods =[pt.get_text() for pt in seven_days_list]           #making a list of the periods

description = seven_days.select(".tombstone-container .short-desc")
short_desc = [pt.get_text() for pt in description]

temp = seven_days.select(".tombstone-container .temp")
temperature = [pt.get_text() for pt in temp]

long_desc = seven_days.select('.tombstone-container img')
long_description = [pt['title'] for pt in long_desc]

#
# print(long_description)
# print(temperature)
# print(periods)
# print(short_desc)

weather_data = pd.DataFrame({
    "Period": periods,
    "Description": long_description,
    "Temperature": temperature,
    "Short Description": short_desc
})

print(weather_data)

