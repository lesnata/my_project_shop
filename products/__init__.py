from flask_restful import Api
from flask import Blueprint

from products.resources import ###

products_bp = Blueprint("products", __name__)
api = Api(products_bp)

products_bp.add_resource(CreateUser, '/users', '/users/<value>')
products_bp.add_resource(Order, '/orders', '/orders/<value>')
products_bp.add_resource(GetMoney, '/user_money', '/user_money/<value>')

