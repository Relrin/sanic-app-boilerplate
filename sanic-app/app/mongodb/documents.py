from umongo import Document
from umongo.fields import StringField

from app import app

instance = app.config["LAZY_UMONGO"]


@instance.register
class Artist(Document):
    name = StringField(required=True, allow_none=False)
