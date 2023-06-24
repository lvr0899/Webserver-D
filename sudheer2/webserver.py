from flask import Flask
#from pymongo import MongoClient
import os,socket

app = Flask(__name__)

@app.route("/")
def hello():
    html = "<h3>Hello {name}!</h3> <b>Hostname:</b> {hostname}<br/>"
    return html.format(name=os.getenv("NAME", ", this is web1"), hostname=socket.gethostname())

@app.route('/workorders')
def get_workorders():
    client = MongoClient("<mongodb_connection_string>")
    db = client["your_database_name"]
    workorders_collection = db["WorkOrders"]
    workorders = workorders_collection.find()
    case_ids = [wo["WOCaseID"] for wo in workorders]
    return jsonify({"WOCaseIDs": case_ids})

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=4000)
