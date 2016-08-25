from aiohttp.hdrs import METH_GET, METH_POST
from aiohttp.web import Response, Request
from .worker import main_task

async def handle_request(request: Request):
    if request.method == METH_GET:
        return Response(status=200)
    elif request.method == METH_POST:
        data = await request.read()
        if data is not None:
            main_task.delay(data)
        return Response(status=200)
    return Response(body='forbidden, debug_uid=9f11235f', status=403)
