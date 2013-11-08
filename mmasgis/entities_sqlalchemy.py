from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import backref, mapper, relation, sessionmaker
import os
dbfile="regioni.sql"
echo=False

#def __init__(self):
Base = declarative_base()
class Regione(Base):
    """
    A task for your TODO list.
    """
    #using_table_options(useexisting=True) 
    __tablename__='regione'
    nome_regione = Column(String)
    id = Column(Integer, primary_key=True,autoincrement=True)
     
     

    def __repr__(self):
        return "regione: "+self.nome

class Comune(Base):
    #using_table_options(useexisting=True) 
    __tablename__='comune'
    nome_comune=Column(String)
    id=Column(Integer, primary_key=True,autoincrement=True)
    provincia_id=Column(Integer)
   
   
    

   
   
class Provincia(Base):
    """
    A task for your TODO list.
    """
    #using_table_options(useexisting=True) 
    __tablename__='provincia'
    nome_provincia = Column(String)
     
    id = Column(Integer, primary_key=True,autoincrement=True)
    regione_id=Column(Integer)
     
    def __init__(self,nome,provincia):
        self.nome=nome
        self.regione_id=provincia
         #return "regione: "+self.nome
         





     # This is so Elixir 0.5.x and 0.6.x work
     # Yes, it's kinda ugly, but needed for Debian
     # and Ubuntu and other distros.

 
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
