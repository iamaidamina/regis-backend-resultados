from Repositories.RepositoryPartido import RepositoryPartido
from Models.Partido import Partido

class ControllerMesa():
  def __init__(self):
    self.repositoryPoliticalParty = RepositoryPartido()
  
  def index(self):
    return self.repositoryPoliticalParty.findAll()
  
  def create(self,infoPoliticalParty):
    newPoliticalParty = Partido(infoPoliticalParty)
    return self.repositoryPoliticalParty.save(newPoliticalParty)

  def show(self,id):
    thePoliticalParty=Partido(self.repositoryPoliticalParty.findById(id))
    return thePoliticalParty.__dict__

  def update(self,id, infoPoliticalParty):
    politicalPartyActual=Partido(self.repositoryPoliticalParty.findById(id))
    politicalPartyActual.nombre=infoPoliticalParty["nombre"]
    politicalPartyActual.lema=infoPoliticalParty["lema"]
    return self.repositoryPoliticalParty.save(politicalPartyActual)
  
  def delete(self,id):
    return self.repositoryPoliticalParty.delete(id)