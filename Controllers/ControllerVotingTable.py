from Repositories.RepositoryVotingTable import RepositoryVotingTable
from Models.VotingTable import VotingTable

class ControllerVotingTable():
  def __init__(self):
    self.repositoryVotingTable = RepositoryVotingTable()
  
  def index(self):
    return self.repositoryVotingTable.findAll()
  
  def create(self,infoVotingTable):
    newVotingTable = VotingTable(infoVotingTable)
    return self.repositoryVotingTable.save(newVotingTable)

  def show(self,id):
    theVotingTable=VotingTable(self.repositoryVotingTable.findById(id))
    return theVotingTable.__dict__

  def update(self,id, infoVotingTable):
    votingTableActual=VotingTable(self.repositoryVotingTable.findById(id))
    votingTableActual.nid_quantity=infoVotingTable["nid_quantity"]
    return self.repositoryVotingTable.save(votingTableActual)
  
  def delete(self,id):
    return self.repositoryVotingTable.delete(id)