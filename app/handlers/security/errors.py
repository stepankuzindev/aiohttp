from aiohttp.web import HTTPClientError, HTTPException
from app import configuration
from app.responses import error


async def errors_middleware(app, handler):

    show_error_details = configuration.show_error_details

    async def errors_middleware_handler(request):
        # sets arrays in the request object, that can be manipulated to insert or remove cookies for the response.
        try:
            response = await handler(request)
        except HTTPException as e:
            return e
        except HTTPClientError as e:
            return e
        except Exception as ex:
            if show_error_details:
                # return error details to the client
                return error(message=str(ex))
            # hide error details
            return error()

        return response

    return errors_middleware_handler
