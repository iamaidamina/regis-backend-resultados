from flask import Flask
from flask import jsonify
from flask import request
from flask_cors import CORS
import json
from waitress import serve
import pymongo
import certifi



ca = certifi.where()
client = pymongo.MongoClient("mongodb+srv://regis-results-backend:suVSDnNwg18gHZch@cluster0.qtizpuh.mongodb.net/bd-results-microservices?retryWrites=true&w=majority",tlsCAFile=ca)
db = client.test
print(db)
baseDatos = client["bd-results-microservices"]
print(baseDatos.list_collection_names())

app=Flask(__name__)
cors = CORS(app)

from Controllers.ControllerVotingTable import ControllerVotingTable
myControllerVotingTable = ControllerVotingTable()

@app.route("/votingtables",methods=['GET'])
def getVotingTables():
  json=myControllerVotingTable.index()
  return jsonify(json)

@app.route("/votingtables",methods=['POST'])
def createVotingTables():
  data = request.get_json()
  json=myControllerVotingTable.create(data)
  return jsonify(json)

@app.route("/votingtables/<string:id>",methods=['GET'])
def getVotingTable(id):
  json=myControllerVotingTable.show(id)
  return jsonify(json)

@app.route("/votingtables/<string:id>",methods=['PATCH'])
def updateVotingTable(id):
  data = request.get_json()
  json=myControllerVotingTable.update(id,data)
  return jsonify(json)

@app.route("/",methods=['GET'])
def test():
  json = {}
  json["message"]="Server running ..."
  return jsonify(json)

def loadFileConfig():
  with open('config.json') as f:
    data = json.load(f)
  return data



if __name__=='__main__':
  dataConfig = loadFileConfig() 
  print("Server running : "+"http://"+dataConfig["url-backend"]+":" + str(dataConfig["port"]))
  serve(app,host=dataConfig["url-backend"],port=dataConfig["port"])