from PyQt4 import QtCore,QtGui
import re 
# Initialize Qt resources from file resources.py
from sessionClasses import *
from sqlalchemy import MetaData, Column, Table, ForeignKey
from sqlalchemy import *
import sys
#from mmasgisDb_sqlalchemy import *
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import backref, mapper, relation, sessionmaker
from elixir import *
import sqlalchemy
from sqlalchemy.ext import compiler
from sqlalchemy.sql.expression import Executable, ClauseElement
from provincia import *
from environment_constants import *
from sqlalchemy import Column, Integer, Unicode,Unicode, ForeignKey, DateTime,Float,Boolean,String
from sqlalchemy import create_engine,MetaData
from sqlalchemy import MetaData, Column, Table
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import backref, mapper, relation, sessionmaker
from sqlalchemy import *

#from Odict import *
#sys.path.append("/home/giuseppe/eclipse/plugins/org.python.pydev.debug_2.3.0.2011121518/pysrc/")
#from pydevd import *
Base = declarative_base()
class DataSource():
    """
    gestisce le operazioni di lettura e scrittura sulle tabelle del db mmasgis per la gestione degli utenti dei profili, delle aree utente e dei censimenti
    """
    def __init__(self,d1,create=False):
        """
        @param string: connectionstring
        @note: nellla connection string deve essere omesso il nome del db se si vuole che venga creato in automatico 
"root:vilu7240@localhost"
        """
        self.cons=dbCons
        dbfile=d1['uname']+":"+d1['pwddb']+'@'+d1['host']
        print "dbfile",dbfile
        family=d1['familyDb']
        family=self.cons.queries[family]
        #"mysql://"+dbfile
        print "url","{0}://".format(family['family'])+dbfile
        self.engine = create_engine("{0}://".format(family['family'])+dbfile)#+"?charset=utf8&use_unicode=1",convert_unicode=True)
        global metadata
        metadata = MetaData(bind=self.engine)
        
        print "creo il db mmasgisDB"
        try:
            print " try create db"
            if create:
                print "drop db"
                self.engine.execute(family['drop']) #cancello il vecchio db    
                self.engine.execute(family['create']) #create db
            print " db creato"
        except sqlalchemy.exc.ProgrammingError:
            print " il db esiste"
        self.engine.execute(family['use']) # select new db
        Base.metadata.create_all(self.engine)
        Session = sessionmaker(bind=self.engine)
        self.session=Session()
        self.initDB(dbfile)            
        #creo l'utente metmi
        #self.engine.execute("CREATE USER metmi IDENTIFIED BY  'metmi'")
        users=self.engine.execute(family['look4metmi']).first()[0]
        print "users ",users
        if users!=0:
                print "l'utente metmi esiste"
                print "associo a metmi i diritti di amministratore"
                self.engine.execute(family['grant%'])
                print "fatto!"                
        else:
                print "l'utente metmi non  esiste"
                print "provvedo a crearlo"
                self.engine.execute("CREATE USER 'metmi'@ IDENTIFIED BY  'metmi'")
                #devo creare lo stesso utente pure su localhost
                self.engine.execute("CREATE USER 'metmi'@'localhost' IDENTIFIED BY  'metmi'")
                print "creato!"
                print "associo a metmi i diritti di amministratore"
                self.engine.execute(family['grant*'])
                print "fatto!"
                print "creo l'utente amministratore di mmasgis"    
        user=utente()
        user=utente()
        user.nome_utente='amministratore'
        user.password=""
        user.amministratoreAree=1
        user.amministratoreCensimenti=1
        user.amministratoreFunzioni=1
        user.clruolo_id=1
        self.session.add(user)
        print     "setto la password di amministratore",d1['passAdmin']        
        user.password=d1['passAdmin']
        self.session.add(user)
        self.session.flush()
        id_amministratore=user.utente_id
        print "id amministratore",id_amministratore
        print "creo il ruolo amministratore"
        r=ruolo()
        r.nome="amministratore"
        r.clruolo_id=1
        self.session.add(r)
        #rendo l'utente super user per le aree
        area=aree()
        area.amministratore=1
        area.utente_id=id_amministratore
        self.session.add(area)
        #rendo l'utente super user per le funzioni 
        profile=profilo()
        profile.utente_id=id_amministratore
        profile.amministratore=1
        self.session.add(profile)
        dbs=rel_utente_dbmmas()
        dbs.amministratore=1
        dbs.utente_id=id_amministratore
        self.session.add(dbs)
        #rendo l'utente super user per i db
        self.session.commit()
        # rendo metmi amministratore su tutti i db e gli consento di accedere da remoto
        #self.engine.execute("GRANT ALL PRIVILEGES ON *.* TO metmi@'%' IDENTIFIED BY 'metmi' WITH GRANT OPTION")
        #g
        #self.session=Session()    
        
        #self.initDB(dbfile)
        # self.session.query(provincia).count()
        #verifico che la tabella provincia si popolata
        c=self.session.query(provincia).count()
        if c==0:
            print "la tabella 'provincia' non e' ancora popolata"
            print "provvedo a popolare la tabella di servizio provincia"
            n=0
            # create a database connection
            #conn = self.engine.connect()
            #ins=provincia.insert()
            #self.engine.execute("use mmasgisDB")
            for p in province:
                n+=1
                pr=provincia(p[1],p[2])
                self.session.add(pr)
                
                #new_pr=ins.values(sigla=p[1],provincia=p[2])
                #conn.execute(new_pr)
                #self.engine.execute("insert into provincia(sigla,provincia)values({0},{1}".format(p[1],p[2]))
            self.session.commit()
            print "ho inserito {0} province ".format(n)
                

        
    def initDB(self,dbfile):
        """
        @param string:stringa di connessione al db, con il seguente formato di stringa "user:pwd@host/nomedb" esempio root:xxxxx@localhost/parafarmacie
        inizializza il db
        """
        MetaData.bind = "mysql://%s"%dbfile
        
        setup_all() 
        
    def getUserCount(self):
        """ritorna il valore attuale di UserCounter
        @return: int
        """
        c= self.ds.value("UserCounter", 0).toInt()[0]
        return c 
    
    def updateProfiles(self,userQname,profile):
        """ aggiorna il profilo utente, memorizzato nell'oggetto profiles
        @param User.qSettingsName: identificativo univoco dell'utente nel sistema nel formato user\d+
        @param {classesObject.qName:classesObject}: 
        """
        if self.ds.contains("profiles"):
            #recupero il dizionario dei profili
            profiles=self.ds.value("profiles").toPyObject()
            print profiles
        else:
            #creo un dizionario dei profili
            profiles=Relations()
        profiles.setCategory("profiles")
        profiles.updateRelations(userQname,profile)
        self.ds.setValue(profiles.getCategory(),profiles)
        
    def getUser(self, uname,pwd):
        """ritorna l'utente identificato da uname e password
        @param string: user-name
        @param string: password
        @return: User
        """
        for u in self.session.query(utente).filter_by(nome_utente=uname).filter_by(password=pwd):
            pass
        user=User(u.nome_utente,u.utente_id)
        user.setProfile(self.getUserProfile(u.utente_id))
        user.setId(u.utente_id)
        user.setRuolo(u.clruolo_id)
        user.setDbs(self.getUserDbs(u.utente_id))
        user.setZone(self.getUserArea(u.utente_id))
        return user
        
    def getUserById(self, Id):
        """ritorna l'utente identificato da uname e password
        @param string: user-name
        @param string: password
        @return: User
        """
        u=self.session.query(utente).filter_by(utente_id=Id).first()
        
        user=User(u.nome_utente,u.utente_id)
        user.setProfile(self.getUserProfile(u.utente_id))
        user.setId(u.utente_id)
        user.setRuolo(u.clruolo_id)
        user.setDbs(self.getUserDbs(u.utente_id))
        user.setZone(self.getUserArea(u.utente_id))
        return user
        
    def updateDbs(self,userQname,profile):
        """ aggiorna i db utente, memorizzati nell'oggetto dbs
        @param User.qSettingsName: identificativo univoco dell'utente nel sistema nel formato user\d+
        @param <{classesObject.qName:classesObject}><int>: 
        """
        if self.ds.contains("dbs"):
            #recupero il dizionario dei profili
            profiles=self.ds.value("dbs").toPyObject()
            print profiles
        else:
            #creo un dizionario dei profili
            profiles=Relations()
        profiles.setCategory("dbs")
        profiles.updateRelations(userQname,profile)
        self.ds.setValue(profiles.getCategory(),profiles)
        
    def updateZones(self,userQname,profile):
        """ aggiorna le aree utente, memorizzate nell'oggetto zones
        @param User.qSettingsName: identificativo univoco dell'utente nel sistema nel formato user\d+
        @param {classesObject.qName:classesObject}: 
        """
        
        if self.ds.contains("zones"):
            #recupero il dizionario dei profili
            profiles=self.ds.value("zones").toPyObject()
            print profiles
            #creo un dizionario dei profili
        profiles=Relations()
        profiles.setCategory("zones")
        profiles.updateRelations(userQname,profile)
        self.ds.setValue(profiles.getCategory(),profiles)
        
    def setZones(self,relations):
        """forza l'oggetto zones di Qsettings
        @param Relations:
        """
        self.ds.setValue("zones",relations)     
        
    
    def registerUser(self,user, qName):
        """
        registra un utente  nel file di sistema con l'etichetta passata come parametro
        @param User:
        @param string: etichetta di identificazione utente
        """
        #aggiorno il profilo memorizzato in profiles
        self.updateProfiles(qName, user.getProfile())
        #aggiorno i dbs memorizzati in dbs
        self.updateDbs(qName, user.getDbs()) #voglio inserire solo le chiavi in Qsettings
        #aggiorno le aree agente 
        self.updateZones(qName, user.getZones)
        #resetto i profili  i db e le zone dell'utente per salvare in Qsettings solo dict vuoti    
        user.resetProfile()
        user.resetDbs()
        user.resetZones()
        self.ds.setValue(qName, user)        
        
        
    def setUserCounter(self,c):
        """setta il valore di UserCount
        @param int: nuovo valore di userCount
        """
        self.ds.setValue("userCounter",c) 
        
    def setDbCounter(self,c):
        """setta il valore di DbCounter
        @param int: nuovo valore di userCount
        """
        self.ds.setValue("dbCounter",c)         
        
        
    def getDbCount(self):
        """ritorna il valore attuale di dbCounter
        @return: int
        """
        c= self.ds.value("dbCounter",0).toInt()[0]
        return c 
    
    def insertUser(self,nome,cl,passwd):
        """
        inserisce un utente nel db
        @param string:nome utente
        @param int: clruolo_id
        @param string: password
        @attention: perche' le modifiche siano permanenti occorre invocare commitOperations
        """ 
        user=utente()
        user.nome_utente=nome
        user.password=passwd
        user.clruolo_id=cl 
        self.session.add(user)
        
    def countUsers(self):
        """
        ritorna il numero di utenti registrati nel db
        @return: int
        """
        c=self.session.query(utente).count()
        return c
    
    def getUserDbs(self,user_id):
        """ritorna i db regfistrati ad un utente
        @return: <[string]> per l'utenteordinario<int> per l'utente root
        """
        profile=[]            #self.session.query(Pv).filter_by(pv_id=Id)
        for p in self.session.query(rel_utente_dbmmas).filter_by(utente_id=user_id):
            print "db registrato", p.db_id
            profile.append(p.db_id)
        #se un utente e' amministratore tutte le righe di profilo hanno settato amministratore a 1
            if p.amministratore==1:
                profile=-1
        else:
            return []
        return profile
    
    def getUserArea(self,user_id):
        """ritorna le aree di pertinenza  di un utente
        @return: <[string]> per l'utenteordinario<int> per l'utente root
        """
        profile=[]            #self.session.query(Pv).filter_by(pv_id=Id)
        for p in self.session.query(aree).filter_by(utente_id=user_id):
            profile.append(p.UTB_id)
            print "trovato area",p.UTB_id
        #se un utente e' amministratore tutte le righe di profilo hanno settato amministratore a 1
            if p.amministratore==1:
                profile=-1
        else:
            return []
        return profile
    
    def getUserProfile(self,user_id):
        """ritorna il profilo di un utente
        @return: <[int]> per l'utenteordinario<int> per l'utente root
        """
        profile=[]            #self.session.query(Pv).filter_by(pv_id=Id)
        for p in self.session.query(profilo).filter_by(utente_id=user_id):
            profile.append(p.funzione_id)
        #se un utente e' amministratore tutte le righe di profilo hanno settato amministratore a 1
        if p.amministratore==1:
            profile=-1
        return profile
    
    def setAreaAdministrator(self,user_id,amministratore):
        """
        rende l'utente amministratore per le aree
        @param int:utente_id
        @param bool:se True setta l'utente come amministratore 
        @note: invocare commitOperations per rendere permanenti le modifiche
        """
        l=lambda y:1 if y==True else 0
        for p in self.session.query(aree).filter_by(utente_id=user_id):     
            p.amministratore=l(amministratore)    
    
    def setProfileAdministrator(self,user_id,amministratore):
        """
        rende l'utente amministratore per le funzioni
        @param int:utente_id
        @param bool:se True setta l'utente come amministratore 
        @note: invocare commitOperations per rendere permanenti le modifiche
        """
        l=lambda y:1 if y==True else 0
        for p in self.session.query(profilo).filter_by(utente_id=user_id):     
            p.amministratore=l(amministratore)    
            
    def setDbsAdministrator(self,user_id,amministratore):
        """
        rende l'utente amministratore per i db
        @param int:utente_id
        @param bool:se True setta l'utente come amministratore 
        @note: invocare commitOperations per rendere permanenti le modifiche
        """
        l=lambda y:1 if y==True else 0
        for p in self.session.query(rel_utente_dbmmas).filter_by(utente_id=user_id):     
            p.amministratore=l(amministratore)    
            
    def isDbAdministrator(self,user_id):
        """ verifica chel'utente sia amministratore per i censimenti
        @param int:user_id
        @return: bool
        """
        a=self.session.query(utente).filter_by(utente_id=user_id).first()
        if a.amministratoreCensimenti!=1:
            return False
        else:
            return True
            
    def isAreaAdministrator(self,user_id):
        """ verifica chel'utente sia amministratore per le aree
        @param int:user_id
        @return: bool
        """
        a=self.session.query(utente).filter_by(utente_id=user_id).first()
        if a.amministratoreAree!=1:
            return False
        else:
            return True
            
    def isFunctionAdministrator(self,user_id):
        """ verifica chel'utente sia amministratore per le funzioni
        @param int:user_id
        @return: bool
        """
        a=self.session.query(utente).filter_by(utente_id=user_id).first()
        if a.amministratoreFunzioni!=1:
            return False
        else:
            return True
            
    """def addCensimento(self,name,censimento,versione, ins_utente):
            nome_db=Column(String(10))
    censimento=Column(Integer)
    versione=Column(Integer)
    ins_data=Column(DateTime)
    mod_data=Column(DateTime)
    ins_utente=Column(Integer)
    mod_utente=Column(Integer)"""
    
    def addArea(self,utente_id,area_id,administrator=False):
            """
            aggiunge una funzione/abilita al profilo dell'utente
            @param int:utente_id
            @param string:signature della UTB 
            @param bool opzionale:  se True setta a uno il campo amministratore della riga inserita in rel_utente_funzione
            @note: il campo amminisatratore della tabella profilo e' settato a 0 di default, cioe' come se fosse un utente ordinario
            @note: il parametro amministratore dovrebbe avere ilvalore ottenuto invocando isAdministrator
            @attention: perche' le modifiche siano permanenti occorre invocare commitOperations
            """
            p=aree()
            p.utente_id=utente_id
            p.UTB_id=area_id
            if administrator:
                p.amministratore=1
            p.amministratore=0 #0 e' il valore di default per l'utente ordinario
            self.session.add(p)
    
    def addFunction(self,utente_id,funzione_id,administrator=False):
            """
            aggiunge una funzione/abilita al profilo dell'utente
            @param int:utente_id
            @param int:function_id  
            @param bool opzionale:  se True setta a uno il campo amministratore della riga inserita in rel_utente_funzione
            @note: il campo amminisatratore della tabella profilo e' settato a 0 di default, cioe' come se fosse un utente ordinario
            @note: il parametro amministratore dovrebbe avere ilvalore ottenuto invocando isAdministrator
            @attention: perche' le modifiche siano permanenti occorre invocare commitOperations
            """
            p=profilo()
            p.utente_id=utente_id
            p.funzione_id=funzione_id
            if administrator:
                p.amministratore=1
            p.amministratore=0 #0 e' il valore di default per l'utente ordinario
            self.session.add(p)
            
    def addDb(self,user_id,db_id,administrator=False):
            """
            aggiunge una funzione/abilita al profilo dell'utente
            @param int:utente_id
            @param int:function_id  
            @param bool opzionale:  se True setta a uno il campo amministratore della riga inserita in rel_utente_funzione
            @note: il campo amminisatratore della tabella profilo e' settato a 0 di default, cioe' come se fosse un utente ordinario
            @note: il parametro amministratore dovrebbe avere ilvalore ottenuto invocando isAdministrator
            @attention: perche' le modifiche siano permanenti occorre invocare commitOperations
            """
            p=rel_utente_dbmmas()
            p.utente_id=user_id
            p.db_id=db_id
            if administrator:
                p.amministratore=1
            p.amministratore=0 #0 e' il valore di default per l'utente ordinario
            self.session.add(p)
            
    def removeFunction(self,user_id,function_id):
        """rimuove una funzione dal profilo utente
        @param int: utente_id
        @param int:funzione_id
        @attention: rimuovere una funzione non ha effetto se l'utente e' amministratore
        """
        for f in self.session.query(profilo).filter_by(utente_id=user_id).filter_by(funzione_id=function_id):
            self.session.delete(f) 
            
    def removeDb(self,user_id,db_Id):
        """rimuove un db  da i dbs a sua disposizione
        @param int: utente_id
        @param int:funzione_id
        @attention: rimuovere una funzione non ha effetto se l'utente e' amministratore
        """
        for f in self.session.query(rel_utente_dbmmas).filter_by(utente_id=user_id).filter_by(db_id=db_Id):
            self.session.delete(f) 
            
    def removeArea(self,user_id,area_id):
        """rimuove un'area dalle zone utente
        @param int: utente_id
        @param string:UTB_signature
        @attention: rimuovere una funzione non ha effetto se l'utente e' amministratore
        """
        for f in self.session.query(aree).filter_by(utente_id=user_id).filter_by(UTB_id=area_id):
            self.session.delete(f) 
    
    def commitOperations(self):
        """
        esegue il commit dellasessione
        """
        self.session.commit()
        
    def isRegistered(self, uname,pwd):
        """ verifica che le credenziali siano corrette
        @param string: nome utente
        @param string:password
        @return: bool: True se le credenziali coincidono con quelle di un utente registrato
        """ 
        u=self.session.query(utente).filter_by(nome_utente=uname).filter_by(password=pwd).count()
        if u!=0:
            return True
        else:
            return False
        
        
    def parser(self,txt,pattern):
        """ ritorna la lista di tutte le occorrenze del pattern nella stringa passata
        @param string:  stringa da esaminare
        @param string:  pattern da applicare
        @return: [string]
        """
        match=re.compile(pattern)
        return match.findall(txt)    
    
    def getObject(self,uname):    
        """ritorna l'oggetto registrato con uname
        @param string: username come appare nella lista  di QSettings
        @return User
        """
        return self.ds.value(uname).toPyObject()
        
    def getUserList(self):
        """ ritorna la lista degli utenti registrati
        @return  [User]
        """
        self.chiavi=self.ds.allKeys()    
        userNames=[ str(i) for i in self.parser(self.chiavi.join("|"), "\user\d+")]
        users=[]
        for i in userNames:
            users.append(self.getObject(i))
        return users
    
    def removeDBs(self):
        """rimuove i db registrati nel sistema
        """
        self.chiavi=self.ds.allKeys()    
        dbNames=[ str(i) for i in self.parser(self.chiavi.join("|"), "db\d+")]
        for db in dbNames:
            self.ds.remove(db)    
            

    def getDbList(self):
        """ ritorna la lista degli utenti registrati
        @return  [extendedDb]
        """
        self.chiavi=self.ds.allKeys()    
        dbNames=[ str(i) for i in self.parser(self.chiavi.join("|"), "db\d+")]
        dbs=[]
        for i in dbNames:
            dbs.append(self.getObject(i))
        return dbs    
    
    def registerDb(self,db):
        """registra un db nel sistema
            e incrementa dbCounter
        @param extendedDb:
        """
        self.chiavi=self.ds.allKeys()
        Id=self.ds.value("dbCounter", 0).toInt()[0]
        #registro il db
        #db.setSettingsName("db{0}".format(Id))
        print "registro il db:db{0}".format(Id)
        self.ds.setValue("db{0}".format(Id),db)
        # incremento il contatore
        Id+=1
        self.ds.setValue("dbCounter",Id)
        print "dbCounter",Id


class ruolo(Base):
    __tablename__="tc_clruolo"
    clruolo_id=Column(Integer,primary_key=True,autoincrement=True)
    nome=Column(String(20))


class utente(Base):
    __tablename__="utente"
    utente_id=Column(Integer,primary_key=True,autoincrement=True)
    nome_utente=Column(Unicode(20))
    password=Column(Unicode(10))
    clruolo_id=Column(Integer)
    amministratoreFunzioni=Column(Integer)
    amministratoreCensimenti=Column(Integer)
    amministratoreAree=Column(Integer)


    def __repr(self):
        return "utente: {0}, {1}, id: {2}".format(self.ruolo,self.nome_utente,self.utente_id)
    
    
class dbmmas(Base):
    
    __tablename__="dbmmas"
    db_id=Column(Integer,primary_key=True,autoincrement=True)
    nome_db=Column(String(10))
    censimento=Column(Integer)
    versione=Column(Integer)
    ins_data=Column(DateTime)
    mod_data=Column(DateTime)
    ins_utente=Column(Integer)
    mod_utente=Column(Integer)


    def __repr(self):
        return "dbmmas: {0}, censimento {1}, versione {2}".format(self.nome_db,self.censimento,self.versione)    
    
class funzione(Base):
    __tablename__="funzione"
    funzione_id=Column(Integer,primary_key=True,autoincrement=True)
    categoria=Column(String(10))
    nome=Column(String(20))
    root=Column(Integer)
    def __repr__(self):
        return "funzione:{0},categoria:{1},id:{2} ".format(self.nome,self.categoria,self.funzione_id)
    
class profilo(Base):
    __tablename__="rel_utente_funzione" 
    id=Column(Integer,primary_key=True,autoincrement=True)
    utente_id=Column(Integer,autoincrement=False)
    funzione_id=Column(Integer,autoincrement=False)
    amministratore=Column(Integer)

    
    def __repr(self):
        l=lambda x: "amministratore" if x==1 else "generico"
        return "profilo per utente_id:{0}, tipo: {1}, funzione_id: {2}".format(self.utente_id,l(self.amministratore),self.funzione_id)
    
class provincia(Base):
    
    def __init__(self,pr,nome):
        self.sigla=pr 
        self.provincia=nome
        
    __tablename__="provincia"  
    id=Column(Integer,primary_key=True)
    sigla= Column(String(2))
    provincia=Column(Unicode(25))
        
        
class aree(Base):
    __tablename__="rel_utente_zona"
    id=Column(Integer,primary_key=True,autoincrement=True)
    UTB_id=Column(String(10),autoincrement=False)#in realta' si tratta della featureSignature della feature sullo shapefile
    utente_id=Column(Integer,autoincrement=False)
    amministratore=Column(Integer)

    def __repr(self):
        l=lambda x: "amministratore" if x==1 else "generico"
        return "zona: {0}, pe utente_id:{1}, {2}".format(self.UTB_id,self.utente_id,l(self.amministratore))
    
class rel_utente_dbmmas(Base):
    __tablename__="rel_utente_dbmmas"
    id=Column(Integer,primary_key=True,autoincrement=True)
    utente_id=Column(Integer,autoincrement=False)
    db_id=Column(Integer,autoincrement=False)
    amministratore=Column(Integer)

    def __repr(self):
        l=lambda x: "amministratore" if x==1 else "generico"
        return "dbregistrato: {0} per l'utente{1} {2}".format(self.db_id,self.utente_id,l(self.amministratore))

            