from sanic import Blueprint
from app.redis.api import handle

bp = Blueprint('redis-api')
bp.add_route(handle, '/redis')