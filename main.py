import tkinter as tk
from tkinter import messagebox
import requests

def get_weather():
    city = city_entry.get().strip()
    if not city:
        messagebox.showerror("Error", "Please enter a city name")
        return

    url = f"http://wttr.in/{city}?format=j1"
    try:
        response = requests.get(url)
        if response.status_code != 200:
            raise Exception("Invalid response from weather service")

        weather_data = response.json()

        # Geçerli hava durumu verilerini kontrol et
        if 'current_condition' not in weather_data or not weather_data['current_condition']:
            raise Exception("Invalid city name or no weather data available")

        current_temp = weather_data['current_condition'][0]['temp_C']
        weather_desc = weather_data['current_condition'][0]['weatherDesc'][0]['value']

        result_label.config(text=f"Temperature: {current_temp}°C\nDescription: {weather_desc}")

        city_entry.delete(0, tk.END)
        root.after(5000, reset_weather)



    except Exception as e:
        messagebox.showerror("Error", f"Could not retrieve weather data: {e}")

def reset_weather():
    result_label.config(text="")

root = tk.Tk()
root.title("Weather App")

root.geometry("400x250")

city_label = tk.Label(root, text="City", font=("Arial", 15))
city_label.pack(pady=10)

city_entry = tk.Entry(root, font=("Arial", 15))
city_entry.pack(pady=10)

get_weather_button = tk.Button(root, text="Check the Weather", command=get_weather, font=("Verdana", 15))
get_weather_button.pack(pady=10)

result_label = tk.Label(root, text="", font=("Verdana", 15))
result_label.pack(pady=20)

root.mainloop()
