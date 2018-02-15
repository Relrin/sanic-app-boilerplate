from sanic import Sanic
from mongomotor import connect

from app.extensions.base import BaseExtension


class MongoDbExtension(BaseExtension):
    app_attribute = 'mongodb'

    def init_app(self, app: Sanic, *args, **kwargs):

        @app.listener('before_server_start')
        async def mongodb_configure(app_inner, _loop):
            client = connect(host=app_inner.config['MONGODB_URI'])
            setattr(app_inner, self.app_attribute, client)

        @app.listener('after_server_stop')
        async def mongodb_free_resources(app_inner, _loop):
            client = setattr(app_inner, self.app_attribute, None)

            if client:
                client.disconnect()
