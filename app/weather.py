from models.weather_data import Weather_Data


class WeatherApp:

    def __init__(self):

        self.weather_data = Weather_Data


    def show_weather(self, city):
        city = city.lower()

        if city not in self.weather_data:
            print("Invalid City Name!")
            return  


        data = self.weather_data[city]

        print("Weather Report :")
        print("City", city.title())
        print("Current_weather", data["current_weather"])
        print("Wind_Speed", data["wind_speed"])
        print("Weather after 1 Hour", data["after_1_hour"])
    


