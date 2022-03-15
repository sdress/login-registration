from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
# if many to many or one to many relationship, may need to import other model

# insert name of schema
db = 'user_registration_schema'

class User:
    def __init__(self, data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.password = data['password']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        # insert other required fields as shown in schema
    
    # CRUD BELOW

    # create method
    @classmethod
    def create(cls, data):
        # some query
        query = "INSERT INTO users (name, created_at, updated_at) VALUES ( %(name)s, NOW(), NOW() );"
        return connectToMySQL(db).query_db(query, data)
    
    # read
    @classmethod
    def get_all(cls):
        query = "SELECT * FROM users;"
        results = connectToMySQL(db).query_db(query)
        all_list = []
        for row in results:
            all_list.append( cls(row) )
        return all_list
    
    @classmethod
    def get_one(cls, data):
        query = "SELECT * FROM users WHERE id = %(id)s;"
        results = connectToMySQL(db).query_db(query, data)
        if len(results) < 1:
            return False
        return cls(results[0])
    
    # update
    @classmethod
    def update(cls, data):
        query = "UPDATE users SET name = %(name)s WHERE id = %(id)s;"
        return connectToMySQL(db).query_db(query, data)
    
    # delete
    @classmethod
    def delete(cls, data):
        query = "DELETE FROM users WHERE id = %(id)s;"
        return connectToMySQL(db).query_db(query, data)
    
    #basic validation form
    @staticmethod
    def validate_survey(data):
        is_valid = True # we assume this is true
        query = "SELECT * FROM users WHERE id = %(id)s"
        results = connectToMySQL(db).query_db(query, data)
        if len(results) >= 1:
            flash("ID already exists")
            is_valid = False
        if len(data['first_name']) < 3:
            flash("First name is a required field.")
            is_valid = False
        if len(data['last_name']) < 3:
            flash("Last name is a required field.")
            is_valid = False
        return is_valid