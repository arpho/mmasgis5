class dbCons:
    queries={}
    mysql5={}
    mysql4={}
    postgresql={}
    queries['mysql4']=mysql4
    queries['mysql5']=mysql5
    queries['mysql']=mysql5
    queries['postgresql']=postgresql
    mysql4['family']='mysql'
    mysql5['family']='mysql'
    postgresql['family']='postgresql'
    mysql5['drop']="drop DATABASE if exists mmasgisDB"
    mysql5['create']="CREATE DATABASE mmasgisDB collate utf8_bin"
    mysql5['use']="USE mmasgisDB"
    mysql4['use']="USE mmasgisDB"
    postgresql['use']="connect mmasgisdb"
    mysql5['look4metmi']="select count(user),host, user, password from mysql.user where user='metmi'"
    mysql5['grant%']="GRANT ALL PRIVILEGES ON *.* TO 'metmi'@ IDENTIFIED BY  'metmi' "
    mysql5['grant*']="GRANT ALL PRIVILEGES ON *.* TO 'metmi'@'localhost' IDENTIFIED BY  'metmi' with GRANT OPTION"
    mysql5['existDb']="SELECT SCHEMA_NAME FROM INFORMATION_SCHEMA.SCHEMATA WHERE SCHEMA_NAME = '%s'"
    mysql4['existDb']="SELECT SCHEMA_NAME FROM INFORMATION_SCHEMA.SCHEMATA WHERE SCHEMA_NAME = '%s'"
    mysql4['drop']="drop DATABASE if exists mmasgisDB"
    mysql4['create']="CREATE DATABASE mmasgisDB"
    mysql4['use']="USE mmasgisDB"
    mysql4['use']="USE mmasgisDB"
    mysql4['look4metmi']="select count(user),host, user, password from mysql.user where user='metmi'"
    mysql4['grant%']="GRANT ALL PRIVILEGES ON *.* TO 'metmi'@ IDENTIFIED BY  'metmi' "
    mysql4['grant*']="GRANT ALL PRIVILEGES ON *.* TO 'metmi'@'localhost' IDENTIFIED BY  'metmi' with GRANT OPTION"