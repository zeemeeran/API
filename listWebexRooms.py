import requests
import json
import time

# Define a local variable in Python that will hold 
# your Authentication API Token:

accessToken = "Bearer MDM5OWI5MTktY2Q3OS00YzM5LTk4MzctNDUyZGUzNzczZmNjNzNhZmVkMWQtMzEw_P0A1_efac7f9c-e9f9-4bda-98f5-e03619b831bc"

# Using the requests library, create a new HTTP GET Request against the 
# Webex Teams API Endpoint for Webex Teams Rooms:
# The local object "r" will hold the returned data:
r = requests.get(   "https://api.ciscospark.com/v1/rooms",
                    headers={'Authorization':accessToken}
                )
# Check if the response from the API call was OK (resp. code 200)
if(r.status_code != 200):
    print("Something wrong has happened:")
    print("ERROR CODE: {} \nRESPONSE: {}".format(r.status_code, r.text))
    assert()

def setHeaders():         
	spark_header = {'Authorization': accessToken, 
                    'Content-Type': 'application/json; charset=utf-8'}
	return spark_header

def getRooms(theHeader):    
	uri = 'https://api.ciscospark.com/v1/rooms'  
	resp = requests.get(uri, headers=theHeader)
	return resp.json()

header = setHeaders()
value = getRooms(header)

# See what is in the JSON data:

jsonData = r.json()

print(
    json.dumps(
        jsonData,
        indent=4
    )
)

rooms = jsonData['items']
for room in rooms:
    print ("Room name: '" + room['title'] + "' ID: " + room['id'])

# Define a variable that will hold the roomId 
roomIdToMessage = None

while True:
    roomNameToSearch = input('Enter full or partial name of the room to find: ')
    rooms = jsonData['items']
    for room in rooms:
        if(room['title'].find(roomNameToSearch) != -1):
            print ("Found rooms with the word " + roomNameToSearch)
            print ("Room name: '" + room['title'] + "' ID: " + room['id'])
            roomIdToMessage = room['id']
            roomTitleToMessage = room['title']
            break

    if(roomIdToMessage == None):
        print("Did not find a room with " + roomNameToSearch + " in it.")
        print("\nPlease try again...")
    else:
        break