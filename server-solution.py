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

# Specifications:
# IOT device sends data to endpoint /setWeight
#       * Sends POST request containing JSON object: {"weight":xxx}
#       * Must save the weight to an SQL database
# User needs weight displayed on dashboard -> endpoint /weight
#       *Get latest weight measurement from database
#       *Display using Jinja
# Another user needs an API endpoint to get the weight in JSON format - /getWeight
#       * Format must be the same as supplied by the IOT device


app = Flask(__name__)


#Add /setWeight endpoint
@app.route("/setWeight", methods=["POST"])
def setWeight():

    obj = request.get_json()
    weight = obj["weight"]
    write_to_db(weight)
    return

#Add /getWeight endpoint
@app.route("/getWeight", methods=["GET"])
def getWeight():

    weight = read_from_database()
    obj = {"weight": weight}
    return json.dumps(obj)

# Add /weight endpoint
@app.route("/weight", methods=["GET"])
def weight():

    weight = read_from_database()
    return render_template("index.html", weight=weight)



app.run()



