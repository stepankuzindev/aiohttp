from functools import wraps
from app.requests import is_ajax
from aiohttp.web import HTTPNotFound


def ajax(f):
    """
    Enforces the use of AJAX requests to access a resource. (Raises HTTPNotFound otherwise)
    """

    @wraps(f)
    async def wrapped(request):
        if not is_ajax(request):
            raise HTTPNotFound()

        return await f(request)

    return wrapped
