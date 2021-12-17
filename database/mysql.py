import mysql.connector

def get_connection():
    return mysql.connector.connect(
        host = "localhost", 
        user = "root", 
        password = "password", 
        database = "Sistema"
        )

def close_resource(resource):
    if resource and hasattr(resource, 'close'):
        resource.close()
