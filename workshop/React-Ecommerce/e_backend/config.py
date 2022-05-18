from configparser import ConfigParser
    

config = ConfigParser()

config['DATABASE'] = {
    'NAME'  : 'recommerce',
    'USER' : 'root',
    'PASSWORD' : 'water',
    'HOST' : 'localhost',
    'PORT' : '3306',
}

with open('config.cfg','w') as config_file:
    config.write(config_file)
