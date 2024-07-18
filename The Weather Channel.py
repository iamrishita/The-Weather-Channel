from tkinter import *
import tkinter as tk
from geopy.geocoders import Nominatim
from tkinter import ttk,messagebox
from timezonefinder import TimezoneFinder
from datetime import datetime
import requests
import pytz

root = Tk()
root.title("The Weather Channel")
root.geometry("900x500+300+200")
root.resizable(False, False)

def getWeather():
    try:
        city=textfield.get()

        geolocator= Nominatim(user_agent="geoapyExercises")
        location= geolocator.geocode(city)
        obj=TimezoneFinder()
        result = obj.timezone_at(lng=location.longitude,lat=location.latitude)
        print(result)

        home = pytz.timezone(result)
        local_time = datetime.now(home)
        current_time = local_time.strftime("%I:%M %p")
        clock.config(text=current_time)
        name.config(text="CURRENT WEATHER")

        #weather
        api="https://api.openweathermap.org/data/2.5/weather?q="+city+"&appid=48b43465bfec45bdf9bcde06064458e0"

        json_data = requests.get(api).json()
        condition = json_data['weather'][0]['main']
        description = json_data['weather'][0]['description']
        temp =int(json_data['main']['temp']-273.15)
        pressure = json_data['main']['pressure']
        humidity = json_data['main']['humidity']
        wind = json_data['wind']['speed']

        t.config(text=(temp,"°"))
        c.config(text=(condition,"|","FEELS","LIKE",temp,"°"))

        W.config(text=wind)
        H.config(text=humidity)
        D.config(text=description)
        P.config(text=pressure)

    except Exception as e:
            messagebox.showerror("Weather App","Invalid Entry!!")
   
    
    



    
#Search box
Search_image = PhotoImage(file="Copy of search.png")
myimage = Label(image=Search_image)
myimage.place(x=20, y=20)

textfield = tk.Entry(root, justify='center', width=17, font=('poppins', 25, 'bold'), bg="#404040", border=0, fg="white")
textfield.place(x=50, y=40)
textfield.focus()

Search_icon = PhotoImage(file="Copy of search_icon.png")
myimage_icon = Button(image=Search_icon, borderwidth=0, cursor="hand2", bg="#203243",command=getWeather)
myimage_icon.place(x=400, y=34)

#logo
image_icon = PhotoImage(file="forecast image.png")
root.iconphoto(False, image_icon)

Round_box = PhotoImage(file="forecast image.png")
Label(root, image=Round_box).place(x=156, y=110)

#Bottom Box
Frame_image=PhotoImage(file="Copy of box.png")
frame_myimage=Label(image=Frame_image)
frame_myimage.pack(padx=5,pady=5,side=BOTTOM)

#time
name=Label(root,font=("arial",15,"bold")) 
name.place(x=30,y=100)
clock=Label(root,font=("Helvetica",20))
clock.place(x=50,y=175)


# label
label1 = Label(root, text="Wind", font=("Helvetica",15,'bold'),fg="white",bg="#1ab5ef")
label1.place(x=100, y=400)

label2 = Label(root, text="Humidity", font=("Helvetica", 15,'bold'), fg="white",bg="#1ab5ef")
label2.place(x=250, y=400)

label3 = Label(root, text="Pressure", font=("Helvetica", 15,'bold'), fg="white",bg="#1ab5ef")
label3.place(x=430, y=400)

label4 = Label(root, text="Description", font=("Helvetica", 15,'bold'), fg="white",bg="#1ab5ef")
label4.place(x=650, y=400)

t=Label(font=("arial",70,"bold"),fg="#ee666d")
t.place(x=400,y=150)
c=Label(font=("arial",15,'bold'))
c.place(x=400,y=250)

W=Label(text="...",font=("arial",20,"bold"),bg="#1ab5ef")
W.place(x=120,y=430)
H=Label(text="...",font=("arial",20,"bold"),bg="#1ab5ef")
H.place(x=280,y=430)
P=Label(text="...",font=("arial",20,"bold"),bg="#1ab5ef")
P.place(x=450,y=430)
D=Label(text="...",font=("arial",20,"bold"),bg="#1ab5ef")
D.place(x=670,y=430)








root.mainloop()
