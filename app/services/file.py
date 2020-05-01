import typing as tp
from datetime import datetime

from sqlalchemy.exc import SQLAlchemyError, DataError
from api.requests.classes import File as ApiFile
from api.responses.errors import DataBaseConnecitonError, DataBaseDataError
from database.models import FileDetail, File, User
from database.models.setting import Session


class FileService():

    def __init__(self, file: tp.Type[ApiFile]):

        self.file = file

    def save_file(self) -> dict:

        try:
            session = Session()

            created_at = datetime.now()

            user = User(name=self.file.user_name,
                        created_at=created_at, updated_at=created_at)

            file = File(users=user, name=self.file.name,
                        created_at=created_at, updated_at=created_at)

            session.add(user)
            session.add(file)

            details = [{'row': d.row, 'contents': d.contents, 'updated_at': created_at,
                        'created_at': created_at} for d in self.file.details]
            session.execute(FileDetail.__table__.insert(), details)

            session.commit()

            result = {'message': 'Success'}
        except DataError:
            raise DataBaseDataError
        except SQLAlchemyError:
            raise DataBaseConnecitonError

        return result
