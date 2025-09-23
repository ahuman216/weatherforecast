import config
import requests

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
            response = requests.get(f"https://api.openweathermap.org/data/2.5/weather?units={self.units}&lat={self.lat}&lon={self.lon}&appid={config.api_key}")
        except:
            print("no internet")

        self.response_json = response.json()
        self.temp = self.response_json["main"]["temp"]
        self.temp_min = self.response_json["main"]["temp_min"]
        self.temp_max = self.response_json["main"]["temp_max"]

    def tempPrint(self):
        print(f"In {self.name} it is currently {self.temp}°{self.printUnits}")
        print(f"Today's high: {self.temp_max}°{self.printUnits}")
        print(f"Today's low: {self.temp_min}°{self.printUnits}")

        

city1 = City("Seoul", 37.566, 126.9784)
city1.tempPrint()

city2 = City("Piscataway", 40.560806, -74.465591, "imperial")
city2.tempPrint()

#add a section with google maps geocoding api for location to weather.
# geocode api requires billing
