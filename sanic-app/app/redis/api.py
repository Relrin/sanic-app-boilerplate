from sanic import Blueprint, response


async def handle(request):
    with await request.app.redis as redis:
        await redis.set('test-my-key', 'value')
        val = await redis.get('test-my-key')
    return response.text(val.decode('utf-8'))
