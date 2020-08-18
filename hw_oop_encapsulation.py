class Weather():
    def __init__(self, dd, mm, yy, minTemp, maxTemp, s):
        self.date = {"day": dd, "month": mm, "year": yy}
        self.temperature = {'minTemp': minTemp, 'maxTemp': maxTemp, 'avgTemp': round((minTemp + maxTemp) / 2)}
        self.sky = s
        
        
    def __str__(self):
        
        import calendar
        mm = calendar.month_abbr[self.date['month']]

        return f"\nWHEATHER [{self.date['day']}. {mm}. {self.date['year']}],\n\n\
        \rTEMPERATURE:\n\
        \rMinimum {self.temperature['minTemp']}C,\n\
        \rMaximum {self.temperature['maxTemp']}C,\n\
        \rAverage {self.temperature['avgTemp']}C\n\n\
        \rThe sky:  is {self.sky}\n"
    
    def __gt__(self, value):
        return self.temperature['avgTemp'] > value.temperature['avgTemp']
    
    def __lt__(self, value):
        return self.temperature['avgTemp'] < value.temperature['avgTemp']
    
    def __eq__(self, value):
        return self.temperature['avgTemp'] == value.temperature['avgTemp'] and self.sky == value.sky
    
    def __ne__(self, value):
        return self.temperature['avgTemp'] != value.temperature['avgTemp'] or self.sky != value.sky

###### CONSUMED

todays_wheather = Weather(17, 8, 2020, 35, 35, 'clear')
tomorrows_weather = Weather(18, 8, 2020, 20, 10, 'clear')

print(todays_wheather)
print(tomorrows_weather)

if todays_wheather != tomorrows_weather:
    print(f"The weather today differs from tomorrow!")

if todays_wheather > tomorrows_weather:
    print("Today is hotter than it will be TOMORROW!")

if todays_wheather < tomorrows_weather:
    print("Tomorrow is warmer than today!")

if todays_wheather == tomorrows_weather:
    print("The weather tomorrow will be like TODAYS!!")

