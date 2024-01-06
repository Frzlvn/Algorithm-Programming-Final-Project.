# Import The required important module for make the App
# tkinter for GUI
# request for make HTPP request
# PIL for processing display image
import tkinter as tk
import requests
from tkinter import messagebox
from PIL import Image, ImageTk
import ttkbootstrap

# a Function to get weather information from OpenWeatherMap API
# that take the weather data from OpenWeatherMap API
# and return it into form containing icon, url , weather decripton, city name and country
def get_weather(city):
    API_key = "9af44cec22a7fc5dc906cf5722f649be"
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_key}"
    res = requests.get(url)

    if res.status_code == 404:
        messagebox.showerror("ERROR", "City or Country not found")
        return None
    
    # parse the response JSON to get weather information
    weather = res.json()
    icon = weather['weather'][0]['icon']
    temperature = weather['main']['temp'] - 273.15
    description = weather['weather'][0]['description']
    city = weather['name']
    country = weather['sys']['country']

    # to get icon URL and retun all the weather information from the API
    icon_url = f"https://openweathermap.org/img/wn/{icon}@2x.png"
    return (icon_url, temperature, description, city, country)

# a fungtion to search weather for a city
# a user input dor text search widget to call and get weather fungtion and weather data for a spesific city
# and also update the GUI with the new weather data
def search():
    city = city_name.get()
    result = get_weather(city)
    if result is None:
        return
    # if the city is found, unpack the weather information
    icon_url, temperature, description, city, country = result
    location_name.configure(text=f"{city}, {country}")

    # get the weather icon image from the API url and update the icon label
    image = Image.open(requests.get(icon_url, stream=True).raw)
    icon = ImageTk.PhotoImage(image)
    icon_Weather.configure(image=icon)
    icon_Weather.image = icon

    # to update the temperature and description labels
    Temperature_Weather.configure(text=f"Temperature: {temperature:.2f}°C")
    Description_Weather.configure(text=f"Description: {description}")


# main program
# for GUI window
root = ttkbootstrap.Window(themename="morph")
root.title("Cuaca App")
root.geometry("400x400")

# Entry widget to enter the city name
city_name = ttkbootstrap.Entry(root, font="Helvetican, 18")
city_name.pack(pady=10)

# Button widget to search the weather information
search = ttkbootstrap.Button(root, text="Search", command=search, bootstyle="warning")
search.pack(pady=10)

# Label widget to " SHOW THE CITY OR COUNTRY NAME "
location_name = tk.Label(root, font="Helvetica, 25")
location_name.pack(pady=20)

# Label widget to " SHOW THE WEATHER ICON "
icon_Weather = tk.Label(root)
icon_Weather.pack()

# Label widget to " SHOW THE TEMPERATURE "
Temperature_Weather = tk.Label(root, font="Helvetica, 20")
Temperature_Weather.pack()

# Label widget to " SHOW THE WEATHER DESCRIPTION "
Description_Weather = tk.Label(root, font="Helvetica, 20")
Description_Weather.pack()

root.mainloop()