#!/usr/bin/python
# -*- coding: latin-1 -
from sqlalchemy import Column, Integer, Unicode,Unicode, ForeignKey, DateTime,Float,Boolean
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import backref, mapper, relation, sessionmaker

echo=False

#def __init__(self):
Base = declarative_base()

class Pv(Base):
	__tablename__='pv'
	pv_id =Column('pv_id',Integer,  primary_key=True)
	codice = Column(Unicode)
	pref_mmas =Column(Unicode)
	cod_mmas =Column(Integer)
	certificato =Column(Boolean)
	pv_mt  =  Column(Boolean)
	cliente=  Column(Boolean)
	cod_cliente  =Column(Unicode)
	ragione_sociale =Column('nome1', Unicode(50))
	titolare	=Column('nome2', Unicode(50))
	tc_istat_id=Column(Integer)
	indirizzo	=Column(Unicode(100))
	cap  =Column(Unicode)
	comune	=Column(Unicode)
	provincia	=Column(Unicode(2))
	tel1	=Column(Unicode(20))
	tel2	=Column(Unicode(20))
	tel3	=Column(Unicode(20))
	cf_pi	=Column(Unicode)
	fax	=Column(Unicode)
	sito =Column(Unicode)
	email  =Column(Unicode)
	note	=Column(Unicode)
	data_aggiornamento	=Column(DateTime)
	tc_stato_id	=Column(Integer)
	ins_data	=Column(DateTime)
	ins_utente	=Column(Integer)
	mod_data	=Column(DateTime)
	mod_utente   =Column(Integer)

class rel_pv_pot(Base):
	#using_table_options(useexisting=True) 
	__tablename__='rel_pv_pot'
	tc_clpot_id=Column(Integer)
	ins_data =Column(DateTime)
	ins_utente =Column(Integer)
	mod_data =Column(DateTime)
	mod_utente =Column(Integer)
	pv_id=Column(Integer,primary_key=True)
	tc_pot_id =Column(Integer,primary_key=True)
	valore =Column(Float)

class tc_clpot(Base):
	__tablename__='tc_clpot'
	tc_clpot_id=Column(Integer,primary_key=True)
	testo=Column(Unicode(255))
	tc_stato_id=Column(Integer)
	primario=Column(Boolean)
	calc_autom=Column(Boolean)
	valore_min=Column(Float)
	ordine=Column(Integer)
	ins_data =Column(DateTime)
	ins_utente =Column(Integer)
	mod_data =Column(DateTime)
	mod_utente =Column(Integer)
	
class tc_pot(Base):
	__tablename__='tc_pot'
	tc_pot_id=Column(Integer, primary_key=True)
	tc_clpot_id=Column(Integer)
	testo =Column(Unicode(255))
	tc_stato_id=Column(Integer)
	ordine= Column(Integer)
	coeff_min=Column(Float)
	coeff_max=Column(Float)
	ins_data =Column(DateTime)
	ins_utente =Column(Integer)
	mod_data =Column(DateTime)
	mod_utente =Column(Integer)

class rel_pv_par(Base):
	__tablename__='rel_pv_par'
	ins_data	=Column(DateTime)
	ins_utente  =Column(Integer)
	mod_data	=Column(DateTime)
	mod_utente  =Column(Integer)
	pv_id =Column(Integer, primary_key=True)
	tc_clpar_id=Column(Integer)
	tc_par_id=Column(Integer, primary_key=True)
	
class  tc_par(Base):
	__tablename__='tc_par'
	tc_par_id =Column(Integer, primary_key=True)
	tc_clpar_id=Column(Integer)
	testo=Column(Unicode(255))
	tc_stato_id=Column(Integer)
	ordine=Column(Integer)
	ins_data	=Column(DateTime)
	ins_utente  =Column(Integer)
	mod_data	=Column(DateTime)
	mod_utente  =Column(Integer)


class tc_clpar(Base):
	__tablename__='tc_clpar'
	tc_clpar_id= Column(Integer,primary_key=True)
	tc_stato_id= Column(Integer)
	testo=Column(Unicode(255))
	ordine=Column(Integer)
	ins_data	=Column(DateTime)
	ins_utente  =Column(Integer)
	mod_data	=Column(DateTime)
	mod_utente  =Column(Integer)
	
	

class rel_pv_mar(Base):
	__tablename__='rel_pv_mar'
	pv_id=Column(Integer,primary_key=True)
	tc_clmar_id=Column(Integer, primary_key=True)
	ordine=Column(Integer,primary_key=True)
	uso=Column(Float)
	tc_mar_id=Column(Integer)
	ins_data	=Column(DateTime)
	ins_utente  =Column(Integer)
	mod_data	=Column(DateTime)
	mod_utente  =Column(Integer)

	def __repr__(self):
			return "pv_id: %s,tc_clmar_id: %s, uso:%s, ordine: %s"%(self.pv_id,self.tc_clmar_id,self.uso,self.ordine)

class tc_mar(Base):
	__tablename__='tc_mar'
	tc_mar_id=Column(Integer,primary_key=True)
	testo=Column(Unicode(255))
	tc_stato_id=Column(Integer)
	ins_data	=Column(DateTime)
	ins_utente  =Column(Integer)
	mod_data	=Column(DateTime)
	mod_utente  =Column(Integer)
	
	def __repr__(self):
		return "testo: %s, tc_mar_id: %d"%(self.testo,self.tc_mar_id)

class tc_clmar(Base):
	__tablename__='tc_clmar'
	tc_clmar_id=Column(Integer,primary_key=True)
	tc_stato_id=Column(Integer)
	testo=Column(Unicode(255))
	ordine=Column(Integer)
	ins_data	=Column(DateTime)
	ins_utente  =Column(Integer)
	mod_data	=Column(DateTime)
	mod_utente  =Column(Integer)
	
	def __repr__(self):
		return "%s tc_clmar_id: %s, ordine: %s"%(self.testo,self.tc_clmar_id,self.ordine)


class tc_rel_clmar_mar(Base):
	__tablename__='tc_rel_clmar_mar'
	tc_clmar_id=Column(Integer, primary_key=True)
	tc_mar_id=Column(Integer,primary_key=True)
	ins_data	=Column(DateTime)
	ins_utente  =Column(Integer)
	mod_data	=Column(DateTime)
	mod_utente  =Column(Integer)
	
	def __repr__(self):
		return "tc_clmar_id: %s,tc_mar_id:%s"%(self.tc_clmar_id,self.tc_mar_id)

			
	 
