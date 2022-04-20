from tkinter import *
from winreg import QueryReflectionKey
from PIL import ImageTk, Image
import requests
import json

root=Tk()
root.title("WEATHER APPLICATION CONNECTING TO API")
root.iconbitmap("icony/camera.ico")
root.geometry("600x100")

zip=Entry(root, width=30)
zip.grid(row=0, column=0, pady= (10,0),sticky=W+E+S+N)

#ZIP Button command function
def ziplook():
    
    try:
        api_request=requests.get("https://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode=" + zip.get() + "&distance=5&API_KEY=6FC24919-B3A4-4754-8CFD-319D64BACE69")
        api=json.loads(api_request.content)
        city=api[0]['ReportingArea']
        quality=api[0]['AQI']
        category=api[0]['Category']['Name']

        #conditional statements for background colors

        if category=="Good":
            weather_color="#0C0"
        elif category=="Moderate":
            weather_color="#FFFF00"
        elif category=="Unhealthy for sensitive Groups":
            weather_color="#ff9900"
        elif category=="Unhealthy":
            weather_color="#FF0000"
        elif category=="Very Unhealthy":
            weather_color="#990066"
        elif category=="Hazardous":
            weather_color="#660000"
        
        root.configure(background=weather_color)
        
        my_label=Label(root, text= city + " Air Quality: "+ str(quality)+ " "+category, 
        font=("Helvetica", 20), background=weather_color)
        my_label.grid(row=1, column=0, columnspan=2)


    except Exception as e:
        api="Error ........."

#https://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode=89129&distance=5&API_KEY=6FC24919-B3A4-4754-8CFD-319D64BACE69

#create zip Button and Entry
zip=Entry(root, width=30)
zip.grid(row=0, column=0, pady= (10,0),sticky=W+E+S+N)
zip_btn=Button(root, text="Input ZIP Code", command=ziplook)
zip_btn.grid(row=0, column=1, pady= (10,0), sticky=W+E+S+N)
root.mainloop()