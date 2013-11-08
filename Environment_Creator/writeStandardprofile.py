from DataSourceUser import *
from profilo import *
def test():
    db=Db('mmasgisDB',-1)
    db.setUserName("root")
    db.setPassword("vilu7240")
    db.setHost("localhost")
    db.setPort("3306")
    db.setRDBMS("mysql")  
    user=User("data",1)      
    user.setActiveDb(db)
    ds=DataSource(user,True)
    ds.writeProfile(profili[0],1)
    
test()
print "finito"