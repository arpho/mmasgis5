from CreateDb import *
from Istat import * 
from regioni import *
from comuni import *
from province import *
class createDbMysql(CreateDb):
	def __init__(self,utonto,create):
		CreateDb.__init__(self,utonto)
		self.engine = create_engine("{0}://".format(self.family['family'])+self.dbfile)#+"?charset=utf8&use_unicode=1",convert_unicode=True)
		
		metadata = MetaData(bind=self.engine)
		try:
			print "createdbMysql line 9",self.family['family']
			#self.engine.execute(self.family['use'])
		except sqlalchemy.exc.DatabaseError:
			print "db non esiste"
		#self.data=data
		
	def createDb(self,utonto,data,create=True):	
		#self.engine.execute(self.family['create'])
		#self.engine.execute(self.family['use'])
		print "creo il db mmasgisDB"
		try:
			print " try create db"
			if create:
				print "drop db"
				#cons= self.engine.connect()
				#cons.connection.connection.set_isolation_level(0)
				
				#self.engine.execute(self.family['drop']) #cancello il vecchio db	

				self.engine.execute(self.family['drop']) #cancello il vecchio db
				self.engine.execute(self.family['create']) #create db
				self.engine.execute(self.family['use'])
				Base.metadata.create_all(self.engine)
				
				#cons.connection.connection.set_isolation_level(1)
			print " db creato"
		except sqlalchemy.exc.ProgrammingError:
			print sqlalchemy.exc.ProgrammingError
			print " il db esiste"
		try:
			self.engine.execute(self.family['use']) # select new db
		except sqlalchemy.exc.OperationalError:
			print "db non esiste"
		Base.metadata.create_all(self.engine)
		Session = sessionmaker(bind=self.engine)
		self.session=Session()
		#self.initDB(dbfile)			
		#creo l'utente metmi
		#self.engine.execute("CREATE USER metmi IDENTIFIED BY  'metmi'")
		users=self.engine.execute(self.family['look4metmi']).first()[0]
		print "users ",users
		if users!=0:
				print "l'utente metmi esiste"
				print "associo a metmi i diritti di amministratore"
				self.engine.execute(self.family['grant%'])
				print "fatto!"				
		else:
				print "l'utente metmi non  esiste"
				print "provvedo a crearlo"
				self.engine.execute(self.family['grant%'])
				#devo creare lo stesso utente pure su localhost
				self.engine.execute("CREATE USER 'metmi'@'localhost' IDENTIFIED BY  'metmi'")
				print "creato!"
				print "associo a metmi i diritti di amministratore"
				self.engine.execute(self.family['grant*'])
				print "fatto!"
				print "creo l'utente amministratore di mmasgis"	
		user=utente()
		user=utente()
		user.nome_utente=data['admin']
		user.azienda_id=1
		user.password=""
		user.amministratore=1
		user.clruolo_id=1
		self.session.add(user)
		user.password=data['adminPass']
		self.session.add(user)
		self.session.flush()
		id_amministratore=user.utente_id
		r=ruolo()
		r.nome="amministratore"
		r.clruolo_id=1
		self.session.add(r)
		#aggiungo una riga alla tabella azienda
		az=company()
		az.nome_azienda="home"
		self.session.add(az)
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
		for f in functions:
			F=funzione()
			F.categoria=f['classe']
			F.nome=f['nome']
			self.session.add(F)
		for n,p in enumerate(profili):
			self.writeProfile(p, n+1)
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
				pr=provincia(p[1],p[2].upper())
				self.session.add(pr)
				
				#new_pr=ins.values(sigla=p[1],provincia=p[2])
				#conn.execute(new_pr)
				#self.engine.execute("insert into provincia(sigla,provincia)values({0},{1}".format(p[1],p[2]))
				
			self.populateIstat()
			print "popolata tabella istat"
			self.populateRegioni()
			print "popolata tabella regioni"
			self.populateProvince()
			print "popolata tabella province"
			self.populateComuni()
			print "popolata tabella comuni"
			self.session.commit()
			#print "ho inserito {0} province ".format(n)
			
	def populateComuni(self):
		for i in comuni:
			c=comuniIstat(i[0],i[1],i[2],i[3])
			self.session.add(c)
			
	def populateRegioni(self):
		for r in regioni:
			p= regioniIstat(r[0],r[1],r[2])
			self.session.add(p)
			
	def populateIstat(self):
		for r in IstatData:
			i=Istat(r[0],r[1],r[2],r[3])
			self.session.add(i)
			
	def populateProvince(self):
		for p in provinceIstat:
			pr= provinciaIstat(p[0],p[1],p[2],p[3],p[4])
			self.session.add(pr)
		self.session.commit()
			#(codice_regione,codice istat from shapefile,nome,sigla,codice istat per pv)
	def writeProfile(self,p,profile_id,company_id=1):
			profilo=profilo_std()
			profilo.nome_profilo=p['nome']
			profilo.azienda_id=company_id
			profilo.amministratore=p['amministratore']
			profilo.profilo_id=profile_id
			self.session.add(profilo)
			self.session.flush()
			self.session.refresh(profilo)
			profilo_Id=profilo.profilo_id
			for i in  p['funzioni']:
				rpf=rel_profilo_funzioni()
				rpf.profilo_id=profilo_Id
				rpf.funzione_id=i
				self.session.add(rpf)
			self.session.commit()
