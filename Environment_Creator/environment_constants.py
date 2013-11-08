class dbCons:
    queries={}
    mysql5={}
    mysql4={}
    postgres={}
    mssql={}
    queries['mysql4']=mysql4
    queries['mysql5']=mysql5
    queries['mysql']=mysql5
    queries['postgresql']=postgres
    queries['mssql']=mssql
    mysql4['family']='mysql'
    mysql5['family']='mysql'
    mssql['family']='mssql'
    postgres['family']='postgresql'
    postgres['create']='CREATE DATABASE "mmasgisDB"  template=template0 '
    postgres['drop']="drop database IF EXISTS mmasgisDB "
    mssql['drop']="drop database IF EXISTS mmasgisDB "
    mysql5['drop']="drop DATABASE if exists mmasgisDB"
    mysql5['create']="CREATE DATABASE mmasgisDB collate utf8_bin"
    mysql5['use']="USE mmasgisDB"
    mssql['use']="USE mmasgisDB"
    mysql4['use']="USE mmasgisDB"
    postgres['use']=" mmasgisDB"
    postgres['grant%']="CREATE ROLE metmi LOGIN ENCRYPTED PASSWORD 'md5078f74b9b3937d5dd35d717074668277'  SUPERUSER CREATEDB   VALID UNTIL 'infinity'"
    postgres['grant*']="CREATE ROLE metmi LOGIN ENCRYPTED PASSWORD 'md5078f74b9b3937d5dd35d717074668277'  SUPERUSER CREATEDB   VALID UNTIL 'infinity'"
    mysql5['look4metmi']="select count(user),host, user, password from mysql.user where user='metmi'"
    postgres['look4metmi']="SELECT 1 FROM pg_roles WHERE rolname='metmi'"
    mysql5['grant%']="GRANT ALL PRIVILEGES ON *.* TO 'metmi'@ IDENTIFIED BY  'metmi' "
    mysql5['grant*']="GRANT ALL PRIVILEGES ON *.* TO 'metmi'@'localhost' IDENTIFIED BY  'metmi' with GRANT OPTION"
    mysql5['existDb']="SELECT count(SCHEMA_NAME) as c FROM INFORMATION_SCHEMA.SCHEMATA WHERE SCHEMA_NAME = '{0}'"
    mysql4['existDb']="SELECT count(SCHEMA_NAME) as c FROM INFORMATION_SCHEMA.SCHEMATA WHERE SCHEMA_NAME = '{0}'"
    postgres['existDb']="select datname from pg_catalog.pg_database where datname = '{0}'"
    mysql4['drop']="drop DATABASE if exists mmasgisDB"
    mysql4['create']="CREATE DATABASE mmasgisDB collate utf8_bin"
    mysql4['use']="USE mmasgisDB"
    mysql4['use']="USE mmasgisDB"
    mysql4['look4metmi']="select count(user),host, user, password from mysql.user where user='metmi'"
    mysql4['grant%']="GRANT ALL PRIVILEGES ON *.* TO 'metmi'@ IDENTIFIED BY  'metmi' "
    mysql4['grant*']="GRANT ALL PRIVILEGES ON *.* TO 'metmi'@'localhost' IDENTIFIED BY  'metmi' with GRANT OPTION"
