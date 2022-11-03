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

# Voting Table CRUD
from Controllers.ControllerMesa import ControllerMesa
myControllerVotingTable = ControllerMesa()

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

@app.route("/votingtables/<string:id>",methods=['DELETE'])
def deleteVotingTable(id):
  json=myControllerVotingTable.delete(id)
  return jsonify(json)

# Political Party CRUD
from Controllers.ControllerPartido import ControllerPartido
myControllerPoliticalParty = ControllerPartido()

@app.route("/politicalparties",methods=['GET'])
def getPoliticalParties():
  json=myControllerPoliticalParty.index()
  return jsonify(json)

@app.route("/politicalparties",methods=['POST'])
def createPoliticalParty():
  data = request.get_json()
  json=myControllerPoliticalParty.create(data)
  return jsonify(json)

@app.route("/politicalparties/<string:id>",methods=['GET'])
def getPoliticalParty(id):
  json=myControllerPoliticalParty.show(id)
  return jsonify(json)

@app.route("/politicalparties/<string:id>",methods=['PATCH'])
def updatePoliticalParty(id):
  data = request.get_json()
  json=myControllerPoliticalParty.update(id,data)
  return jsonify(json)

@app.route("/politicalparties/<string:id>",methods=['DELETE'])
def deletePoliticalParty(id):
  json=myControllerPoliticalParty.delete(id)
  return jsonify(json)

# Political Candidate CRUD
from Controllers.ControllerCandidato import ControllerCandidato
myControllerCandidate = ControllerCandidato()

@app.route("/politicalcandidates",methods=['GET'])
def getPoliticalCandidates():
  json=myControllerCandidate.index()
  return jsonify(json)

@app.route("/politicalcandidates",methods=['POST'])
def createPoliticalCandidate():
  data = request.get_json()
  json=myControllerCandidate.create(data)
  return jsonify(json)

@app.route("/politicalcandidates/<string:id>",methods=['GET'])
def getPoliticalCandidate(id):
  json=myControllerCandidate.show(id)
  return jsonify(json)

@app.route("/politicalcandidates/<string:id>",methods=['PATCH'])
def updatePoliticalCandidate(id):
  data = request.get_json()
  json=myControllerCandidate.update(id,data)
  return jsonify(json)

@app.route("/politicalcandidates/<string:id>",methods=['DELETE'])
def deletePoliticalCandidate(id):
  json=myControllerCandidate.delete(id)
  return jsonify(json)

@app.route("/politicalcandidates/<string:id>/politicalparties/<string:id_partido>",methods=['PUT'])
def asignarPartidotoACandidato(id,id_partido):
  json=myControllerCandidate.asignarPartido(id,id_partido)
  return jsonify(json)

# Resultado CRUD
from Controllers.ControllerResultado import ControllerResultado
myControllerResult = ControllerResultado()

@app.route("/votingresults",methods=['GET'])
def getResults():
  json=myControllerResult.index()
  return jsonify(json)

@app.route("/votingresults/<string:id>",methods=['GET'])
def getResult(id):
  json=myControllerResult.show(id)
  return jsonify(json)

@app.route("/votingresults/mesa/<string:id_mesa>/candidato/<string:id_candidato>",methods=['POST'])
def createResult(id_mesa,id_candidato):
  data = request.get_json()
  json=myControllerResult.create(data,id_mesa,id_candidato)
  return jsonify(json)

@app.route("/votingresults/<string:id_resultado>/mesa/<string:id_mesa>/candidato/<string:id_candidato>",methods=['PATCH'])
def updateResult(id_resultado,id_mesa,id_candidato):
  data = request.get_json()
  json=myControllerResult.update(id_resultado,data,id_mesa,id_candidato)
  return jsonify(json)

@app.route("/votingresults/<string:id_resultado>",methods=['DELETE'])
def deleteResult(id_resultado):
  json=myControllerResult.delete(id_resultado)
  return jsonify(json)

#-------------------------------------------------------------------------------------------------------------------------------
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