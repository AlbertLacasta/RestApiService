from flask_restful import Resource


class user(Resource):
    def get(self):
        return {"message": "Hello, from User!"}
       
