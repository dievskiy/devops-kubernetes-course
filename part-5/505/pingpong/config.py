import os


class Config(object):
    PORT = os.getenv('PORT', 8080)
    HOST = os.getenv('HOST', 'localhost')
    POSTGRES_DB = os.environ['POSTGRES_DB']
    POSTGRES_USER = os.environ['POSTGRES_USER']
    POSTGRES_PASSWORD = os.environ['POSTGRES_PASSWORD']
