import configparser

config = configparser.ConfigParser()
config['debug'] = {'STATUS':'True'}
config['allowedhost'] = {'HOST':'*'}
config['database'] = {'ENGINE':'django.db.backends.mysql','NAME':'djangodb','HOST':'127.0.0.1','PORT':'3306','USER':'root','PASSWORD':'water'}

with open('config1.ini', 'w') as configfile:
    config.write(configfile)
