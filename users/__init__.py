from flask_restful import Api
from flask import Blueprint

from users.resources import CreateUser, Order, GetMoney

users_bp = Blueprint("users", __name__)
api = Api(users_bp)

users_bp.add_resource(CreateUser, '/users', '/users/<value>')
users_bp.add_resource(Order, '/orders', '/orders/<value>')
users_bp.add_resource(GetMoney, '/user_money', '/user_money/<value>')

