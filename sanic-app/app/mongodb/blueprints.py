from sanic import Blueprint
from app.mongodb.api import handle

bp = Blueprint('mongodb-api')
bp.add_route(handle, '/mongodb')
