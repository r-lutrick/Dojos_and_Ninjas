from flask_app.config.mysqlconnection import MySQLConnection
from flask_app import DATABASE
# !!! Import controllers FILE to prevent circular import !!!
from flask_app.controllers import dojos_controller as dc
from flask_app.models import ninja_model as nm


# Model for instanciating Dojo data
class Dojo:
    def __init__(self, data):
        self.id = data['id']
        self.name = data['name']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def get_all(cls):
        query = """
            SELECT *
            FROM dojos
        """
        response = MySQLConnection(DATABASE).query_db(query)
        output = []
        if response:
            for row in response:
                output.append(cls(row))
            return output

    @classmethod
    def get_one(cls, data):
        query = """
            SELECT *
            FROM dojos
            LEFT JOIN ninjas
                ON dojos.id = ninjas.dojo_id
            WHERE dojos.id=%(id)s
        """
        response = MySQLConnection(DATABASE).query_db(query, data)
        dojo_data = {
            'id': response[0]['id'],
            'name': response[0]['name'],
            'created_at': response[0]['created_at'],
            'updated_at': response[0]['updated_at']
        }
        print(response)
        dojo_instance = cls(dojo_data)
        ninja_list = []
        if response:
            for row in response:
                ninja_data = {
                    'id': row['ninjas.id'],
                    'first_name': row['first_name'],
                    'last_name': row['last_name'],
                    'age': row['age'],
                    'created_at': row['ninjas.created_at'],
                    'updated_at': row['ninjas.updated_at'],
                    'dojo_id': row['id']
                }
                ninja_instance = nm.Ninja(ninja_data)
                ninja_list.append(ninja_instance)
        dojo_instance.ninjas = ninja_list
        return dojo_instance

    @classmethod
    def add_one(cls, data):
        query = """
            INSERT INTO dojos (name, created_at, updated_at)
            VALUES (%(name)s, NOW(), NOW())
        """
        return MySQLConnection(DATABASE).query_db(query, data)
