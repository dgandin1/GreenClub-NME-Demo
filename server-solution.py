from flask import Flask, request, render_template
import json

#Writes a weight measurement to the database
def write_to_db(weight):

    with open("db.json", "w") as file:
        obj = {"w":weight}
        file.write(json.dumps(obj))

# Reads most recentently recorded weight from the database
def read_from_database():

    with open("db.json", "r") as file:
        return json.loads(file.read())["w"]



app = Flask(__name__)

#From here, client can send POST request setWeight
@app.route("/iot", methods=["GET"])
def iot_client():
    return render_template("iot_client.html")  # Served at /iot for setWeight endpoint

# Specifications:
# IOT device sends data to endpoint /setWeight
#       * Listens for POST request containing the value of the weight
# User needs weight displayed on dashboard -> endpoint /weight
#       *Get latest weight measurement from database
#       *Return Jinja template parameterized on weight
# Another user needs an API endpoint to get the weight in JSON format - /getWeight
#       * Format must be the same as supplied by the IOT device

#Add /setWeight endpoint
@app.route("/setWeight", methods=["POST"])
def setWeight():
    #Get request to the database that returns a dictionary
    obj = request.get_json()
    #Extract value from dictionary
    weight = obj["weight"]
    write_to_db(weight)
    return

#Add /getWeight endpoint
@app.route("/getWeight", methods=["GET"])
#Function to call when visiting the endpoint
def getWeight():
    #Read the data from the database using helper function
    weight = read_from_database()
    #Creates new python object to be returned
    obj = {"weight": weight}
    #Response to the GET request that is returned to the endpoint
    return json.dumps(obj)

# Add /weight endpoint
@app.route("/weight", methods=["GET"])
def weight():
    weight = read_from_database()
    return render_template("index.html", weight=weight)

app.run()



