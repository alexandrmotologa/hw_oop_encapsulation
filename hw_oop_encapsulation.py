class Weather():
    def __init__(self, d, t, s):
        self.date = d
        self.temperature = t
        self.sky = s
    
    def __str__(self):
        return f"WHEATHER[{self.date}]: {self.temperature:3}C, the sky is {self.sky}\n"
    
    # def __gt__(self, value):
    #     return self.temperature > value.temperature
    
    # def __eq__(self, value):
    #     return self.temperature == value.temperature and self.sky == value.sky




###### CONSUMED

todays_wheather = Weather('2020-08-17', 30, 'clear')
tomorrows_weather = Weather('2020-08-18', 30, 'clear')

print(todays_wheather)
print(tomorrows_weather)

# if todays_wheather > tomorrows_weather:
#     print("Today is hotter than it will be TOMORROW!")

# if todays_wheather == tomorrows_weather:
#     print("The weather tomorrow will be like TODAYS!!")