from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models import ninja_model


class Dojo:
    def __init__(self, data):
        self.id = data['id']
        self.name = data['name']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']


#  =============    READ ALL    ============
    @classmethod
    def get_all(cls):
        query = 'SELECT * FROM dojos;'
        results = connectToMySQL('dojos_and_ninjas_schema').query_db(query)
        dojos = []
        if results:
            for row in results:
                this_dojo = cls(row)
                dojos.append(this_dojo)
        return dojos


#  =============    READ ONE    ============
    @classmethod
    def get_one(cls, data):
        query = "SELECT * FROM dojos LEFT JOIN ninjas ON dojos.id WHERE dojos.id = %(id)s;"
        results = connectToMySQL(
            'dojos_and_ninjas_schema').query_db(query, data)
        print("GET ONE RESULTS-------------->", results[0])
        dojo_one = cls(results[0])
        all_ninjas = []
        for row in results:
            ninja_row = {
                'id': row['ninjas.id'],
                'first_name': row['first_name'],
                'last_name': row['last_name'],        # keys of ninja class
                'age': row['age'],
                'created_at': row['created_at'],
                'updated_at': row['updated_at'],
                'dojo_id': row['dojo_id']
            }
            this_ninja = ninja_model.Ninja(ninja_row)
            all_ninjas.append(this_ninja)
        dojo_one.ninjas = all_ninjas
        return dojo_one


#  =============    CREATE    ============
    @classmethod
    def save(cls, data):
        query = """
            INSERT INTO dojos(name)
            VALUES (%(name)s);
        """
        return connectToMySQL('dojos_and_ninjas_schema').query_db(query, data)
