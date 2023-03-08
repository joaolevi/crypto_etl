from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from os import path
from inspect import getfile, currentframe
from yaml import safe_load

class DBSession():
    def __init__(self):
        self.session = None
        self.engine  = None

    def get_main_directory(self):
        return (path.dirname(path.abspath(getfile(currentframe()))))


    def read_config_db_file(self):
        maindirectory = self.get_main_directory()
        try:
            with open(maindirectory + "/../../DBConfig.yaml", 'r') as fileconfig:
                config = safe_load(fileconfig)
        except Exception as e:   
            config = {'login'   : 'postgres', 
                      'password': '1234',
                      'ip'      : 'localhost',
                      'port'    : '5432'}
        return config
    
    def start_db_session(self):
        config = self.read_config_db_file()
        self.engine = create_engine('postgresql://'+ config['login'] +':'+ config['password'] +'@'+ config['ip'] +':'+ config['port'] +'/postgres')
        Session = sessionmaker(bind=self.engine)
        self.session = Session()

    def save_to_db(self, data):
        if (self.session.connection()):
            self.session.add(data)
            self.session.commit()
        else:
            self.start_db_session()
