from Repositories.RepositoryCandidato import RepositoryCandidato
from Repositories.RepositoryPartido import RepositoryPartido
from Models.Candidato import Candidato
from Models.Partido import Partido

class ControllerCandidato():
  def __init__(self):
    self.repositoryCandidate = RepositoryCandidato()
    self.repositoryPoliticalParty = RepositoryPartido()
  
  def index(self):
    return self.repositoryCandidate.findAll()
  
  def create(self,infoCandidate):
    newCandidate = Candidato(infoCandidate)
    return self.repositoryCandidate.save(newCandidate)

  def show(self,id):
    theCandidate=Candidato(self.repositoryCandidate.findById(id))
    return theCandidate.__dict__

  def update(self,id, infoCandidate):
    candidateActual=Candidato(self.repositoryCandidate.findById(id))
    candidateActual.cedula=infoCandidate["cedula"]
    candidateActual.numero_resolucion=infoCandidate["numero_resolucion"]
    candidateActual.nombre=infoCandidate["nombre"]
    candidateActual.apellido=infoCandidate["apellido"]
    return self.repositoryCandidate.save(candidateActual)
  
  def delete(self,id):
    return self.repositoryCandidate.delete(id)
  
  """
  Relación departamento y materia
  """
  def asignarPartido(self,id,id_partido):
    candidateActual=Candidato(self.repositoryCandidate.findById(id))
    partidoActual = Partido(self.repositoryPoliticalParty.findById(id_partido))
    candidateActual.partido=partidoActual
    return self.repositoryCandidate.save(candidateActual)