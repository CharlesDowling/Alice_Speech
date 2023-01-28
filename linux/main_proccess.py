import json,urllib.request
from pytemp import pytemp
import wikipediaapi
from datetime import *
import time

class main_proccess():


    def weather(Type_Of_Info):
        weather_json = json.load(urllib.request.urlopen("https://api.weather.gov/stations/KISP/observations/latest?require_qc=true"))
        Temperature = weather_json["properties"]["temperature"]["value"]
        Cloud_Cover = weather_json["properties"]["textDescription"]
        rain_value = weather_json["properties"]["precipitationLastHour"]["value"]

        if rain_value == None:
            rain_value = 0

        #Details full current weather
        if Type_Of_Info == "temp":
            response = "The temperature is currently" + str(Temperature) + " degrees celcius or " + str(int(pytemp(Temperature,"c","f")))  + " degrees fahrenheit"

        elif Type_Of_Info == "full":
            if int(rain_value) > 0:
                response = "It is currently " + Cloud_Cover + ". The temperature is currently " + str(Temperature) + " degrees celcius or " + str(int(pytemp(Temperature,"c","f")))  + " degrees fahrenheit" + " and it is currently raining"
            else:
                response = "It is currently " + Cloud_Cover + ". The temperature is currently " + str(Temperature) + " degrees celcius or " + str(int(pytemp(Temperature,"c","f")))  + " degrees fahrenheit" + " and it is not currently raining"
        return response

    def what():
        return

    def wiki(Text):
        
        ###Removes Articles
        if Text[:3] == "an ":
            Text = Text[3:]
        if Text[:2] == "a ":
            Text = Text[2:]

        wiki_wiki = wikipediaapi.Wikipedia('simple')
        wiki_page = wiki_wiki.page(Text)
        if wiki_page.exists == True:
            return wiki_page.summary
        else:
            return "I could not find any information about " + Text



    def proccess_text(Text,engine):

        print("XXXXXX")

        wake_word = "alice "

        response = ""

        if Text[:6] == "alice ":

            Text = Text[6:]

            if Text == "get the weather":
                response = main_proccess.weather("full")
            elif Text == "what's the weather":
                response = main_proccess.weather("full")
            elif Text == "What's it like out there":
                response = main_proccess.weather("full") 
            elif Text == "get the temperature":
                response = main_proccess.weather("temp")
            elif Text == "what is the temperature":
                response = main_proccess.weather("temp")

            if Text == "what is your name":
                response = "My name is alice"
            elif Text == "what's your name":
                response = "My name is alice"
            elif Text == "what are you":
                response = "I am an assistant created by Chaz to help you do things on your computer"
            elif Text ==  "what is your purpose":
                response = "I am an assistant created by Chaz to help you do things on your computer"
            elif Text == "what is today's date":
                response = "Today is " + str(date.today())
            elif Text == "what is the time":
                dt = datetime.now()
                hour = dt.strftime("%I")
                if hour[:1] == "0":
                    hour = hour[1:]
                minute = dt.strftime("%M")
                if int(datetime.now().strftime("%H")) > 12 and int(datetime.now().strftime("%H")) < 18:
                    response = "The time is " + hour + minute + "p.m. in the afternoon"
                elif int(datetime.now().strftime("%H")) >= 18:
                    response = "The time is " + hour + minute + "p.m. in the evening"
                else:
                    response = "The time is " + hour + minute + "a.m. in the morning"
            elif Text[:7] == "what is" and response == "":
                response = main_proccess.wiki(Text[8:])
          
                
            
            if Text == "mabel hello":
                response = " hello human" 

            if response == "":
                response = "error"
        
        if response == "":
                response = "error"

        return response

print(main_proccess.weather("full"))
