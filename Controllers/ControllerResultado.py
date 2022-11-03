from Repositories.RepositoryResultado import RepositoryResultado
from Repositories.RepositoryCandidato import RepositoryCandidato
from Repositories.RepositoryMesa import RepositoryMesa
from Models.Resultado import Resultado
from Models.Candidato import Candidato
from Models.Mesa import Mesa

class ControllerResultado():
  def __init__(self):
    self.repositoryResult = RepositoryResultado()
    self.repositoryCandidate = RepositoryCandidato()
    self.repositoryVotingTable = RepositoryMesa()
  
  def index(self):
    return self.repositoryResult.findAll()
  
  def create(self,infoResult, id_mesa, id_candidato):
    newResult = Resultado(infoResult)
    theVotingTable=Mesa(self.repositoryVotingTable.findById(id_mesa))
    theCandidate= Candidato(self.repositoryCandidate.findById(id_candidato))
    newResult.mesa=theVotingTable
    newResult.candidato=theCandidate

    return self.repositoryResult.save(newResult)

  def show(self,id):
    theResult=Resultado(self.repositoryResult.findById(id))
    return theResult.__dict__

  def update(self,id, infoResult, id_mesa, id_candidato):
    theResult=Resultado(self.repositoryResult.findById(id))
    theResult.numero_mesa = infoResult["numero_mesa"]
    theResult.id_partido = infoResult["id_partido"]
    theVotingTable=Mesa(self.repositoryVotingTable.findById(id_mesa))
    theCandidate= Candidato(self.repositoryCandidate.findById(id_candidato))
    theResult.mesa = theVotingTable
    theResult.candidato = theCandidate
    
    return self.repositoryResult.save(theResult)
  
  def delete(self,id):
    return self.repositoryResult.delete(id)
  
