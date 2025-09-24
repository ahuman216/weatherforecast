import requests
import time
import ziptocoord

class City:
    def __init__(self, name, lat, lon, units="metric"):
        self.name = name
        self.lat = lat
        self.lon = lon
        self.units = units
        if units == "imperial":
            self.printUnits = "F"
        if units == "metric":
            self.printUnits = "C"
        if units == "standard":
            self.printUnits = "standard units"
        self.getData()

    def getData(self):
        try:
            response = requests.get(f"https://api.openweathermap.org/data/2.5/weather?units={self.units}&lat={self.lat}&lon={self.lon}&appid=d0c76440181875c27c4053af158e11a6")
        except:
            print("Something went wrong, double check your input and internet connection and try again.")

        self.response_json = response.json()
        self.temp = self.response_json["main"]["temp"]
        self.temp_min = self.response_json["main"]["temp_min"]
        self.temp_max = self.response_json["main"]["temp_max"]

    def tempPrint(self):
        print(f"In {self.name} it is currently {self.temp}° {self.printUnits}")
        print(f"Today's high: {self.temp_max}° {self.printUnits}")
        print(f"Today's low: {self.temp_min}° {self.printUnits}")

        

#city1 = City("Seoul", 37.566, 126.9784)
#city1.tempPrint()

#city2 = City("Piscataway", 40.560806, -74.465591, "imperial")
#city2.tempPrint()
print("________________________________________________________________________________")
time.sleep(1)
print("______________________Welcome to the Temperature Calculator_____________________")
time.sleep(1)
print("__All you have to do is just enter your zipcode and I'll tell you the weather.__")
time.sleep(1)
print("_________________________________Are you ready?_________________________________")
time.sleep(3)
print("_________________________________Are you really?________________________________")
time.sleep(1)
print("---------------------------------Okay, let's go!--------------------------------")
time.sleep(1)
while True:
    try:
        zipcode = input("What is your zipcode? ")
        break
    except:
        print("Enter a valid zipcode")
while True:
    try:
        u = str(input("Do you want imperial, standard or metric units? ")).lower()
        if(u=="metric" or u== "imperial" or u=="standard"):
            break
        else:
            pass
    except:
        print("Not a valid answer. Enter either imperial, standard or metric")


c = ziptocoord.getCoord(zipcode)
lat = c[0]
lon = c[1]
name = c[2]
thecity = City(name, lat, lon, u)
thecity.tempPrint()
time.sleep(1)
print("_____________If you are not in the US, this will not work for you._______________")
time.sleep(1)
print("_______________________If you enjoyed this, try it again!________________________")
time.sleep(1)
print("______________________________Thank you for playing!_____________________________")



