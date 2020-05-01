import json
from flask import Response, request, current_app
from flask_restful import Resource
from marshmallow.exceptions import ValidationError


from api.requests.classes import File
from api.responses.errors import InternalServerError, RequestJsonValidationError
from services.file import FileService


class FileApi(Resource):

    def post(self) -> Response:

        body = request.get_json()

        try:
            file = File.Schema().loads(json.dumps(body))
        except ValidationError:
            current_app.logger.error(f'request : {request.data}')
            raise RequestJsonValidationError()
        except Exception:
            raise InternalServerError()

        file_servise = FileService(file)

        result = file_servise.save_file()

        return result, 200
