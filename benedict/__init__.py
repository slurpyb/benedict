import random
from benedict.name import Name

async def app(scope, receive, send):
    assert scope['type'] == 'http'
    name =  str(Name()).encode('utf-8')
    data = b"%s!\n" % name
    await send({
        'type': 'http.response.start',
        'status': 200,
        'headers': [
            [b'content-type', b'text/plain'],
        ],
    })
    await send({
        'type': 'http.response.body',
        'body': data,
    })