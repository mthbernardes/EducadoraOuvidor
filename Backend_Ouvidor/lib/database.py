from pydal import DAL, Field
import os

class database():
    def __init__(self,dbPath):
        self.dbPath = dbPath

    def create(self,):
        self.migrate = True
        if os.path.exists(os.path.abspath(self.dbPath)):
            self.migrate = False
        self.DATABASE_TYPE = 'sqlite://'
        self.DATABASE = self.DATABASE_TYPE+os.path.abspath(self.dbPath)
        self.db = DAL(self.DATABASE,migrate=self.migrate)
        self.db.define_table('log',
            Field('date',),
            Field('time',),
            Field('phrase')
            )
        return self.db
