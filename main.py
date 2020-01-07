from fastapi import FastAPI
from fastapi.exceptions import RequestValidationError
from starlette.exceptions import HTTPException
from starlette.middleware.cors import CORSMiddleware

from api.errors.http_error import http_error_handler
from api.errors.validation_error import http422_error_handler
from api.routes.api import router as api_router
from core.config import ALLOWED_HOSTS, API_PREFIX, DEBUG, PROJECT_NAME, VERSION
from core.events import create_start_app_handler, create_stop_app_handler

def get_application() -> FastAPI:
    application = FastAPI(title=PROJECT_NAME, debug=DEBUG, version=VERSION)

    application.add_middleware(
        CORSMiddleware,
        allow_origins=ALLOWED_HOSTS or ['*'],
        allow_credentials=True,
        allow_methods=['*'],
        allow_headers=['*'],
    )

    application.add_event_handler('startup', create_start_app_handler(application))
    application.add_event_handler('shutdown', create_stop_app_handler(application))

    application.add_exception_handler(HTTPException, http_error_handler)
    application.add_exception_handler(RequestValidationError, http422_error_handler)

    application.include_router(api_router, prefix=API_PREFIX)

    return application

app = get_application()




'''
HH  HH  EEEEEE  LL      LL      OOOOOO
HH  HH  EE      LL      LL      OO  OO
HHHHHH  EEEE    LL      LL      OO  OO
HH  HH  EE      LL      LL      OO  OO
HH  HH  EEEEEE  LLLLLL  LLLLLL  OOOOOO

CCCCCC  ММ   ММ  ЕЕЕЕЕЕ  ШШ   ШШ  НН  НН   ЯЯЯЯЯ  ВВВВ   КК  КК  ИИ   ИИ
CC      МММ МММ  ЕЕ      ШШ   ШШ  НН  НН  ЯЯ  ЯЯ  ВВ  В  КК КК   ИИ  ИИИ
CC      ММ М ММ  ЕЕЕЕ    ШШ Ш ШШ  НННННН   ЯЯЯЯЯ  ВВВВ   ККК     ИИ И ИИ
CC      ММ   ММ  ЕЕ      ШШ Ш ШШ  НН  НН   ЯЯ ЯЯ  ВВ  В  КК КК   ИИИ  ИИ
CCCCCC  ММ   ММ  ЕЕЕЕЕЕ  ШШШШШШШ  НН  НН  ЯЯ  ЯЯ  ВВВВ   КК  КК  ИИ   ИИ
'''
