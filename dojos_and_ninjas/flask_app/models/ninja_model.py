from flask_app.config.mysqlconnection import connectToMySQL


class Ninja:
    def __init__(self, data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.age = data['age']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        
        

#  =============    READ ALL    ============
    @classmethod
    def get_all(cls):
        query = 'SELECT * FROM ninjas;'
        results = connectToMySQL('dojos_and_ninjas_schema').query_db(query)
        print("GET ALL RESULTS-------------->", results)
        ninjas = []
        if results:
            for row in results:
                this_ninja = cls(row)
                ninjas.append(this_ninja)
        return ninjas


#  =============    READ ONE    ============
    @classmethod
    def get_one(cls,data):
        query = "SELECT * FROM ninjas WHERE id = %(id)s;"
        result = connectToMySQL('dojos_and_ninjas_schema').query_db(query,data)
        print("GET ONE RESULTS-------------->", result[0])
        return result[0]
    
    
#  =============    CREATE    ============
    @classmethod
    def save(cls, data):
        query = """
            INSERT INTO ninjas(first_name, last_name, age, dojo_id)
            VALUES (%(first_name)s,%(last_name)s,%(age)s,%(dojo_id)s);
        """
        return connectToMySQL('dojos_and_ninjas_schema').query_db(query,data)
    
    