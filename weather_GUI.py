from tkinter import *
from tkinter import ttk
import requests

def get_res():
    city = city_name.get()
    api_key = "365ddca7c62cc00cc965fe1a6251d2e7"
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}"
    data = requests.get(url).json()

    # Ensure data contains expected keys
    if "weather" in data and "main" in data:
        # Updating weather climate and description
        label11.config(text=data["weather"][0]["main"])
        label22.config(text=data["weather"][0]["description"])

        # Converting temperature from Kelvin to Celsius
        temp_celsius = data["main"]["temp"] - 273.15
        label33.config(text=f"{temp_celsius:.2f} °C")

        # Displaying pressure
        label44.config(text=data["main"]["pressure"])
    else:
        # If the data does not contain expected keys, set labels to "N/A"
        label11.config(text="N/A")
        label22.config(text="N/A")
        label33.config(text="N/A")
        label44.config(text="N/A")

win = Tk()
win.geometry("500x500")
win.title("Weather App")
win.config(bg="gray")

name_label = Label(win, text="Nayeem Weather App", font=("Times New Roman", 25, "bold"))
name_label.place(x=25, y=40, height=50, width=450)

city_name = StringVar()
list_name = ["Andhra Pradesh", "Arunachal Pradesh", "Assam", "Bihar", "Chhattisgarh", "Goa", "Gujarat", "Haryana",
             "Himachal Pradesh", "Jammu and Kashmir", "Jharkhand", "Karnataka", "Kerala", "Madhya Pradesh",
             "Maharashtra", "Manipur", "Meghalaya", "Mizoram", "Nagaland", "Odisha", "Punjab", "Rajasthan",
             "Sikkim", "Tamil Nadu", "Telangana", "Tripura", "Uttar Pradesh", "Uttarakhand", "West Bengal",
             "Andaman and Nicobar Islands", "Chandigarh", "Dadra and Nagar Haveli", "Daman and Diu", "Lakshadweep",
             "National Capital Territory of Delhi", "Puducherry"]

com = ttk.Combobox(win, values=list_name, font=("Times New Roman", 25, "bold"), textvariable=city_name)
com.place(x=60, y=120, height=45, width=300)

button1 = Button(win, text="Done", font=("Times New Roman", 25, "bold"), command=get_res)
button1.place(x=190, y=190, height=45, width=100)

label1 = Label(win, text="Weather Climate", font=("Times New Roman", 15, "bold"))
label1.place(x=50, y=260, height=45, width=160)
label11 = Label(win, text="", font=("Times New Roman", 15, "bold"))
label11.place(x=290, y=260, height=45, width=160)

label2 = Label(win, text="Weather Desc", font=("Times New Roman", 15, "bold"))
label2.place(x=50, y=320, height=45, width=160)
label22 = Label(win, text="", font=("Times New Roman", 15, "bold"))
label22.place(x=290, y=320, height=45, width=160)

label3 = Label(win, text="Temperature", font=("Times New Roman", 15, "bold"))
label3.place(x=50, y=380, height=45, width=160)
label33 = Label(win, text="", font=("Times New Roman", 15, "bold"))
label33.place(x=290, y=380, height=45, width=160)

label4 = Label(win, text="Pressure", font=("Times New Roman", 15, "bold"))
label4.place(x=50, y=440, height=45, width=160)
label44 = Label(win, text="", font=("Times New Roman", 15, "bold"))
label44.place(x=290, y=440, height=45, width=160)

win.mainloop()
