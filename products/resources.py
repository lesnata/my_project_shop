from flask import json, request
from flask_restful import Resource, marshal_with

from db import db
from marshal import products_structure
from model import Product
from parser import products_parser


class CreateProducts(Resource):
    @marshal_with(products_structure)
    def get(self):
        product_name = products_parser.parse_args().get('name')
        category_name = products_parser.parse_args().get('category')
        store_name = products_parser.parse_args().get('store')
        min_price = products_parser.parse_args().get('min_price')
        max_price = products_parser.parse_args().get('max_price')
        if product_name:
            product = Product.query.filter_by(name=product_name).first()
            return product, 200

        if category_name:
            product = Product.query.filter_by(category=category_name).all()
            return product, 200

        if store_name:
            product = Product.query.filter_by(name=store_name).first()
            return product, 200

        if min_price:
            product = Product.query.filter_by(Product.price >= min_price,
                                              Product.price <= max_price).all()
            return product, 200

        return Product.query.all(), 200
