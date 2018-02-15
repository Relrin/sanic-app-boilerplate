from sanic import Blueprint, response
from mongomotor import Document
from mongomotor.fields import StringField
from marshmallow_mongoengine import ModelSchema


bp = Blueprint('mongodb-api')


class Artist(Document):
    name = StringField()


class ArtistSerializer(ModelSchema):

    class Meta:
        model = Artist



@bp.route('/mongodb')
async def handle(request):
    artist = Artist(name="A new rockstar!")
    await artist.save()
    serializer = ArtistSerializer()
    return response.json(serializer.dump(artist))
