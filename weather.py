"""
Name: SRIHARI CHANDRAMOULI
UTA ID: 1001529776
Programming Language: Python
Version: 3.6
CITATIONS
*********
1. https://docs.python.org/3.4/howto/sockets.html
2. https://docs.python.org/3/library/tkinter.html
3. http://www.diveintopython3.net/xml.html
4. https://www.youtube.com/watch?v=LNYoFo1sdwg
5. https://stackoverflow.com/questions/21179272/parsing-a-url-xml-with-the-the-elementtree-xml-api
6. https://docs.python.org/3.4/library/xml.etree.elementtree.html
7. https://stackoverflow.com/questions/35120250/python-3-get-and-parse-json-api
8. https://stackoverflow.com/questions/23131227/how-to-readlines-from-urllib
"""

import xml.etree.ElementTree as etree
import requests

from tkinter import *
top = Tk()                                          # Creating a Box
L1 = Label(top, text="Enter latitude")              # Creating a label
L1.grid(row=0, column=0)                            # Dimensions of the label
L2 = Label(top, text="Enter Longitude")             # Creating another label
L2.grid(row=1, column=0)                            # Dimensions of the label
E1 = Entry(top, bd = 5)                             # Creating a text field
E1.grid(row=0, column=1)                            # Dimensions
E2 = Entry(top, bd = 5)                             # Creating a text field
E2.grid(row=1, column=1)                            # Dimensions

"""
def connect(latitude, longitude):                   #This function is used to connect to the weather server and it returns the desired values
    url = "https://api.weather.gov/points/"+str(latitude)+","+str(longitude)+"/forecast"    #The url to be connected
    print(url)
    data = requests.get(url).json()                 #Request to get all the details from that url
    print(data)
    print("temperature :"+str(data['properties']['periods'][0]['temperature']))    # Printing the temperature
    print("Wind Speed:"+str(data['properties']['periods'][0]['windSpeed']))         # Printing the wind speed
    print("Wind Direction:"+str(data['properties']['periods'][0]['windDirection'])) # Printing the wind direction
    print("Detailed Forecast:"+str(data['properties']['periods'][0]['detailedForecast']))   #Printing the detailed forecast

"""
def WeatherParser(e1, e2):                                                # This function parses an xml file and retrieves the desired values
    tree = etree.parse('convertjsonweather.xml')                            # XML parsing using ElementTree
    root = tree.getroot()                                                   # Getting the 1st children of the root
    entries = tree.findall('properties')                                    # Finding all the elements known as properties
    list_of_period = entries[0].findall('periods')                          # Finding all the elements known as periods
    # print(root)
    list_of_geog = root.findall('geometry')                                 # Finding all elements known as geometry
    #list_of_prop = root.findall('properties')
    #print (list_of_period)
    #c = list_of_period[0].find('name').text
    #print(c)

    a = list_of_geog[0].find('latitude').text                               # Getting the exact value of the latitude element within geometry
    b = list_of_geog[0].find('longitude').text                              # Getting the exact value of the longitude element within geometry
    # print(a,b)

    print("Enter the period you want to get information: ")
    n = int(input())                                                        # Getting the input for the period of the day

    if float(e1) == float(a) and float(e2) == float(b):                     # Checkong whether the input of the user and the latitude and the longitude value is the same
        print('Day: ' + list_of_period[n+1].find('name').text)                # Printing the Day/Time of the day
        print("Temperature: " + list_of_period[n+1].find('temperature').text) # Printing the temperature
        print("Wind Speed: " + list_of_period[n+1].find('windSpeed').text)    # Printing the wind speed
        print("Wind Direction: " + list_of_period[n+1].find('windDirection').text)    # Printing the wind direction
        print("Forecast: " + list_of_period[n+1].find('detailedForecast').text)       # Printing the forecast
        print("Short Forecast: " + list_of_period[n+1].find('shortForecast').text)     # Printing the short forecast

        print("Do you wish to continue? Y or N")
        r = input()                                                 # Getting the input for either wanting to refresh or not
        if r == 'Y':
            Refresh()                                               # Calling the Refresh()
    else:
        print("Invalid Coordinates")
        exit()


def Refresh():
    WeatherParser(E1.get(), E2.get())               # Calling the WeatherParser() for the refresh activity


#MyButton1 = Button(top, text="Submit", width=10, command=lambda: connect(E1.get(), E2.get()))
MyButton1 = Button(top, text="Submit", width=10, command=lambda: WeatherParser(E1.get(), E2.get()))             #Submit button
MyButton1.grid(row=3, column=0)
#MyButton2 = Button(top, text="Refresh", width=10, command=lambda: connect(E1.get(), E2.get()))
MyButton2 = Button(top, text="Refresh", width=10, command=Refresh)                                              #Refresh Button
MyButton2.grid(row=3, column=2)
top.mainloop()                                                          #Ending the tkinter

#-97.1081, 32.7357