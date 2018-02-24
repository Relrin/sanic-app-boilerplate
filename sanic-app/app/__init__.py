from sanic import Sanic

from sanic_redis_ext import RedisExtension
from sanic_mongodb_ext import MongoDbExtension
from app.redis.blueprints import bp as redis_bp
from app.mongodb.blueprints import bp as mongodb_bp


app = Sanic('sanic-app')
app.config.from_envvar('APP_CONFIG_PATH')

app.redis = RedisExtension(app)
app.mongodb = MongoDbExtension(app)

app.blueprint(redis_bp)
app.blueprint(mongodb_bp)
