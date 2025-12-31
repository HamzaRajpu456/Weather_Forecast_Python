from app.weather import WeatherApp


def main():
    app = WeatherApp()
    city = input("Enter City Name : ")
    app.show_weather(city)


if __name__ == "__main__":
    main()
    


