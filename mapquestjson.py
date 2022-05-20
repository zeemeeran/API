from os import stat
from turtle import st
import requests
import urllib.parse

main_api = "https://www.mapquestapi.com/directions/v2/route?"
#orig = "Washington"
#dest = "Baltimaore"
key = "svFABXuvnSfNWin3151WvkAP9g1qTQIU"

while True:
    orig = input("Enter starting location: ")
    if orig == "quit" or orig == "q":
        break
    dest = input("Destination : ")
    if dest == "quit" or orig == "q":
        break
        
    url = main_api + urllib.parse.urlencode({"key": key, "from":orig, "to":dest})

    print("URL is : ", (url))
    json_data = requests.get(url).json()
    json_status = json_data['info']['statuscode']

    if json_status == 0:
        print("API status: "+ str(json_status) + " = A successful route call.\n")
        print("Directions from " + orig + " to " + dest )
        print("Miles: " + str(json_data['route']['distance']))
        print("Trip duration: " + str(json_data['route']['formattedTime']))
        print("Fuel used (Gal): " + str(json_data['route']['fuelUsed']) + "\n")

        print("Kilometers: " + str("{:.2f}".format(json_data['route']['distance'] * 1.61)))
        print("Trip duration: " + str(json_data['route']['formattedTime']))
        print("Fuel used (Ltr): " + str("{:.2f}".format(json_data['route']['fuelUsed'] * 3.74)) + "\n")
     #   print("Kilometers:      " + str("{:.2f}".format((json_data["route"]["distance"])*1.61)))

        #print(json_data['route']['legs'][0]['maneuvers'][0]['narrative'])

        print("===============================================================\n")

        for each in json_data['route']['legs'][0]['maneuvers']:
            print(each['narrative'] + " (" + str("{:.2f}".format((each['distance'])* 1.61)) + " KM)")
        
        print("\n===============================================================\n")

    elif json_status == 402:
        print("\n****************************************************************")
        print("Status: " + str(json_status) + "; Invalid user input for one or both locations!")
        print("\n****************************************************************")

    else:
        print("\n****************************************************************")
        print("Status: " + str(json_status) + "; Refer to: ")
        print("https://developer.mapquest.com/documentation/directions-api/status-codes")
        print("\n****************************************************************")