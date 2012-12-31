import yql

yqlWeather = yql.WeatherWrapper('<FLICK API KEY>')

''' fetch weather info with co-ordinates '''
result = yqlWeather.getWeatherReportByCoOrdinate(43.666698455811, -79.416801452637)
print(result)

''' fetch weather info with ip '''
result = yqlWeather.getWeatherReportByIP('8.8.8.8')
print(result)
