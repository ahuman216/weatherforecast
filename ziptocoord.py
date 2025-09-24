import requests
def getCoord(zipcode):
    try:
        url = f"http://api.openweathermap.org/geo/1.0/zip?zip={zipcode},US&appid=d0c76440181875c27c4053af158e11a6"
        response = requests.get(url)
        r = response.json()
        lat = r["lat"]
        
        lon = r["lon"]
        name = r["name"]
        return lat, lon, name
    except:
        return [38.8951, -77.0364, "Invalid zipcode, showing temperatures for Washington DC"]
