from flask_restful  import Resource, marshal_with, request
import json
from marshal_structure import users_structure, products_structure
from model import User, Product, OrderProduct

#че это
from parser import users_parser


#дальше прописываем все манипуляции с creat user, get, post, delete