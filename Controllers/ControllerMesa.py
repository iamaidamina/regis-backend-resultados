from Repositories.RepositoryMesa import RepositoryMesa
from Models.Mesa import Mesa

class ControllerMesa():
  def __init__(self):
    self.repositoryVotingTable = RepositoryMesa()
  
  def index(self):
    return self.repositoryVotingTable.findAll()
  
  def create(self,infoVotingTable):
    newVotingTable = Mesa(infoVotingTable)
    return self.repositoryVotingTable.save(newVotingTable)

  def show(self,id):
    theVotingTable=Mesa(self.repositoryVotingTable.findById(id))
    return theVotingTable.__dict__

  def update(self,id, infoVotingTable):
    votingTableActual=Mesa(self.repositoryVotingTable.findById(id))
    votingTableActual.numero=infoVotingTable["numero"]
    votingTableActual.cantidad_inscritos=infoVotingTable["cantidad_inscritos"]
    return self.repositoryVotingTable.save(votingTableActual)
  
  def delete(self,id):
    return self.repositoryVotingTable.delete(id)