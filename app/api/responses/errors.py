from flask_api import status
from resources.message.error import MESSAGE


class InternalServerError(Exception):
    pass


class RequestJsonValidationError(Exception):
    pass


class DataBaseConnecitonError(Exception):
    pass

class DataBaseDataError(Exception):
    pass


Errors = {
    "InternalServerError": {
        "message": MESSAGE['InternalServerError'],
        "status": status.HTTP_500_INTERNAL_SERVER_ERROR
    },
    "RequestJsonValidationError": {
        "message": MESSAGE['RequestJsonValidationError'],
        "status": status.HTTP_400_BAD_REQUEST
    },
    "DataBaseConnecitonError": {
        "message": MESSAGE['DataBaseConnecitonError'],
        "status": status.HTTP_500_INTERNAL_SERVER_ERROR
    },
    "DataBaseDataError":{
        "message":MESSAGE['DataBaseDataError'],
        "status":status.HTTP_500_INTERNAL_SERVER_ERROR
    }
}
