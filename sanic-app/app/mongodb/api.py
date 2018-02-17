from sanic import response


async def handle(request):
    from app.mongodb.documents import Artist
    artist = Artist(name="A new rockstar!")
    await artist.commit()
    return response.json(artist.dump())
