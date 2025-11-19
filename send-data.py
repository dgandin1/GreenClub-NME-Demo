import json

def write_to_db(weight):

    with open("db.json", "w") as file:
        obj = {"w":weight}
        file.write(json.dumps(obj))


write_to_db(input("Enter dummy weight: "))
print("POST request sent!")