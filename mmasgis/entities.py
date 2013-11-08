from elixir import *
import os
dbfile="regioni.sql"
class Regione(Entity):
    """
    A task for your TODO list.
"""
    using_table_options(useexisting=True) 
    using_options(tablename='regione')
    nome = Field(Unicode,required=True)
    id = Field(Integer, colname="id", primary_key=True)
     
     

    def __repr__(self):
        return "regione: "+self.nome

class Comune(Entity):
    using_table_options(useexisting=True) 
    using_options(tablename='comune')
    nome=Field(Unicode)
    id=Field(Integer, colname="id", primary_key=True)
    provincia_id=Field(Integer)

   
   
class Provincia(Entity):
    """
    A task for your TODO list.
    """
    using_table_options(useexisting=True) 
    using_options(tablename='provincia')
    nome = Field(Unicode,required=True)
    id = Field(Integer,default=None,primary_key=True)
    regione_id=Field(Integer)
     

    def __repr__(self):
        return "regione: "+self.nome
         



saveData=None

def initDB():
    metadata.bind = "sqlite:///%s"%dbfile
    metadata.bind.echo = False
    setup_all()
    if not os.path.exists(dbfile):
        create_all()

# This is so Elixir 0.5.x and 0.6.x work
# Yes, it's kinda ugly, but needed for Debian
# and Ubuntu and other distros.

global saveData
import elixir
if elixir.__version__ < "0.6":
    saveData=session.flush
else:
    saveData=session.commit



def main():

# Initialize database
    initDB()
   
    for task in Provincia.query.all():
            
            print task   

    # Create two tags
    #green=Tag(name=u"green")
    #red=Tag(name=u"red")

    #Create a few tags and tag them
    #   d = date.fromordinal(730920)     
    #  tarea1=Task(text=u"Buy tomatos",tags=[red],date=d)
    # tarea2=Task(text=u"Buy chili",tags=[red],date=d)
    #tarea3=Task(text=u"Buy lettuce",tags=[green],date=d)
    #tarea4=Task(text=u"Buy strawberries",tags=[red,green],date=d)
    #saveData()
