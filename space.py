import urllib.request
import json
url = 'http://api.open-notify.org/astros.json'

response = urllib.request.urlopen(url) #I have a webpagee stored with the response
print(response)

data = json.loads(response.read()) #change jSON into python, printable
print(data)

print("success? ", data["message"])

for i in data["people"]: 
    print("\t", i["name"], "is on the", i["craft"])
   
#must send in a query to the server
#program waiting on the server for a query, which will send us back a picture or other type of data

while True:

    url = 'http://api.open-notify.org/iss-now.json'
    response = urllib.request.urlopen(url) 
    data = json.loads(response.read())
    
    print("success: ", data["message"])
    print("latitude ", data["iss_position"]["latitude"])
    print("longittude ", data["iss_position"]["longitude"])
    
