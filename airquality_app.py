import tkinter as tk
import tkinter.ttk as ttk
from PIL import ImageTk, Image
import requests
import json


class WeatherApp(tk.Tk):
    """A weather app that displays air quality data for a given city.

    Attributes:
        city_name (tk.Entry): An entry field for entering the name of a city.
        city_button (ttk.Button): A button for looking up air quality data for the entered city.
        air_quality_menu (tk.OptionMenu): A dropdown menu for selecting the type of air quality data to display.
        selected_air_quality (tk.StringVar): A variable that stores the currently selected air quality option.
        label (tk.Label): A label that displays the air quality data for the selected city.

    Methods:
        city_lookup(): Looks up air quality data for the entered city and displays it in the label.
    """

    def __init__(self):
        """Initializes the WeatherApp with a GUI and default settings."""
        super().__init__()
        self.title("Weather App")
        self.geometry("700x120")
        self.configure(background="#ffffff")
        self.iconbitmap("Icon Image/clouds-outlined-weather-symbol_icon-icons.com_54695.ico")

        # Create a label for the city_name entry field
        city_label = tk.Label(self, text="City Name:")
        city_label.grid(row=0, column=0, sticky=tk.W)

        # Create the city_name entry field
        self.city_name = tk.Entry(self, borderwidth=1)
        self.city_name.grid(row=1, column=0, sticky=tk.W+tk.E+tk.N+tk.S)

        # Create a new style for the button
        self.style = ttk.Style()

        # Configure the custom style for the button
        self.style.configure("Custom.TButton", background="#009966", relief="flat", foreground="#000")

        # Assign the custom style to the button
        self.city_button = ttk.Button(self, text="Lookup A Place", command=self.city_lookup, style="Custom.TButton")

        # Define a new style for the button when the mouse is over it
        self.style.map("Custom.TButton", foreground=[("active", "#555")])

        # Configure the custom style for the button again to update with hover effect
        self.style.configure("Custom.TButton", background="#009966", relief="flat", foreground="#000")

        self.city_button.grid(row=1, column=1, sticky=tk.W+tk.E+tk.N+tk.S)

        self.label = tk.Label(self, font=("Helvetica", 15), background="#ffffff")
        self.label.grid(row=3, column=0, columnspan=2)

        # Create a list of air quality measurement options
        self.air_quality_options = ["PM2.5", "PM10", "NO2", "SO2"]

        # Create a StringVar to store the selected air quality option
        self.selected_air_quality = tk.StringVar(value=self.air_quality_options[0])

        # Create an OptionMenu widget with the list of air quality options and the selected option variable
        self.air_quality_menu = tk.OptionMenu(self, self.selected_air_quality, *self.air_quality_options)
        self.air_quality_menu.grid(row=2, column=0, sticky=tk.W+tk.E+tk.N+tk.S)


    def city_lookup(self):
        """Looks up air quality data for the entered city and displays it in the label.

        Raises:
            Exception: An error occurred while retrieving air quality data.
        """
        try:
            # Fetch the air quality data based on the selected air quality option
            air_quality_option = self.selected_air_quality.get()
            api_request = requests.get(f"https://api.waqi.info/feed/{self.city_name.get()}/?token=YOUR_API_TOKEN")
            api = json.loads(api_request.content)

            if air_quality_option == "PM2.5":
                quality = api['data']['iaqi']['pm25']['v']
            elif air_quality_option == "PM10":
                quality = api['data']['iaqi']['pm10']['v']
            elif air_quality_option == "NO2":
                quality = api['data']['iaqi']['no2']['v']
            elif air_quality_option == "SO2":
                quality = api['data']['iaqi']['so2']['v']

            city = api['data']['city']['name']
            category = api['status']
            

            if quality <= 50: 
                weather_color = "#009966"
            elif quality <= 100:
                weather_color = "#ffde33"
            elif quality <= 150:
                weather_color = "#ff9933"
            elif quality <= 200:
                weather_color = "#cc0033"
            elif quality <= 300:
                weather_color = "#660099"
            else:
                weather_color = "#7e0023"

            if weather_color == "#009966":
                air_condition = "Good"
            elif weather_color == "#ffde33":
                air_condition = "Moderate"
            elif weather_color == "#ff9933":
                air_condition = "Unhealthy for Sensitive Groups"
            elif weather_color == "#cc0033":
                air_condition = "Unhealthy"
            elif weather_color == "#660099":
                air_condition = "Very Unhealthy"
            else:
                air_condition = "Hazardous"

            self.configure(background=weather_color)
            self.label.configure(text=f"{city} - Air Quality - {quality} - {air_condition}")

        except Exception as e:
            self.label.configure(text="Error...")


if __name__ == '__main__':
    app = WeatherApp()
    app.mainloop()


