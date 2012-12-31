''' Weather Plugins for YQL python wrapper  '''
import yql

class WeatherWrapper():
    def __init__(self, FLICKR_API_KEY=None):
        if FLICKR_API_KEY is not None:
            self.FLICKR_API_KEY = FLICKR_API_KEY
        else:
            print("Flickr API Key required. Please signup for flickr api key")
            quit()


    ''' get current weather report with coordinate. 
        This might be useful to show weather report to any webapp if user shares his location vioa browser. '''
    def getWeatherReportByCoOrdinate(self, latitude, longitude):
        query = "SELECT * FROM weather.forecast WHERE woeid IN (SELECT place.woeid FROM flickr.places WHERE lat=@latitude and lon=@longitude AND api_key=@api_key)"
        yqlObject = yql.Public()
        resultObj = yqlObject.execute(query, {
            "latitude": latitude,
            "longitude": longitude,
            "api_key": self.FLICKR_API_KEY
        })
        return resultObj.one()
    
    
    ''' get current weather report with ip. 
        This might be useful to show weather report to any webapp as soon as user send his first request as there app can get the external ip for the user. '''
    def getWeatherReportByIP(self, ipAddress):
        query = "SELECT * FROM weather.forecast WHERE woeid IN (SELECT place.woeid FROM flickr.places WHERE api_key=@api_key AND (lat,lon) IN (SELECT latitude,longitude FROM pidgets.geoip WHERE ip=@ip))"
        yqlObject = yql.Public()
        resultObj = yqlObject.execute(query, {
            "ip": ipAddress,
            "api_key": self.FLICKR_API_KEY
        })
        return resultObj.one()
