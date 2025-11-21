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

# TODO: Add /setWeight endpoint (returns nothing)

# TODO: Add /getWeight endpoint (returns json.dumps(obj))

# TODO: Add /weight endpoint (returns render_template("index.html", weight=weight))

app.run()
