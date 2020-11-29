from flask import Blueprint
from flask_restful import Api
from endpoints.user import user
from endpoints.login import login
from endpoints.register import register


api_bp = Blueprint('api', __name__)
api = Api(api_bp)

# API Route/endpoints
api.add_resource(user, '/user')
api.add_resource(login, '/login')
api.add_resource(register, '/register')
