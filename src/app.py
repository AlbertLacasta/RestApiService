from flask import Blueprint
from flask_restful import Api
from endpoints.user import user

api_bp = Blueprint('api', __name__)
api = Api(api_bp)

# API Route/endpoints
api.add_resource(user, '/user')
