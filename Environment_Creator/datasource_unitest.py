from DataSourceUser import *
from MySQLdb import *
import unittest

class TestSequenceFunctions(unittest.TestCase):
    def setUp(self):
        user={'uname':'root','pwddb':'vilu7240','passAdmin':'metmi'}
        user['familyDb']='mysql5'
        user['host']='localhost'
        
        self.ds=DataSource(user,True)
        
    def gtestgetFunction(self):
        print self.ds.getFunctions()
        
    def htestGetItemUtente(self):
        print self.ds.getItemUtente(1).nome_utente
        
    def gtestCreateNewUser(self):
        print self.ds.createNewUser()
        
    def htestCreateNewProfile(self):
        print self.ds.createNewProfile()
        
    def ntestGetRDU(self):
        print "rdu",self.ds.getRDU(1,1)
        
    def testGetAllProfile(self):
        print "profili",self.ds.getAllProfile(1)
    def ltestGetUsers(self):
        print self.ds.getAllRDU(1,1)
    
    def ftestNameExistTrue(self):
        self.assertTrue(self.ds.isNametaken('amministratore',1), "non trova amministratore")
        
    def testgetUserDBs(self):
        print self.ds.getUserDbs(7)
        #print self.ds.getUserDbs(7,True)
        
    def vtestNameExistFalse(self):
        self.assertFalse(self.ds.isNametaken('amministratore',2), " trova amministratore")
        
    def testGetAllDb(self):
        print "db",self.ds.getUserDbRelations(1)
        
    def dtestGetDbs(self):
        print self.ds.getDbs(1)
        
    def testCreateRDU(self):
        print self.ds.createNewRDU()
if __name__ == '__main__':
    unittest.main()