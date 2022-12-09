from flask_app.config.mysqlconnection import MySQLConnection
from flask_app import DATABASE
# !!! Import controllers FILE to prevent circular import !!!


# Model for instanciating Ninja data
class Ninja:
    def __init__(self, data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.age = data['age']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.dojo_id = data['dojo_id']

    # Class Method for adding a ninja to the DB
    @classmethod
    def add_one(cls, data):
        query = """
            INSERT INTO ninjas (first_name, last_name, age, created_at, updated_at, dojo_id)
            VALUES (%(first_name)s,%(last_name)s,%(age)s, NOW(), NOW(),%(dojo_id)s)
        """
        return MySQLConnection(DATABASE).query_db(query, data)
