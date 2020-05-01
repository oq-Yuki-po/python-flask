import typing as tp

from sqlalchemy.exc import SQLAlchemyError, DataError
from api.requests.classes import File as ApiFile
from api.responses.errors import DataBaseConnecitonError, DataBaseDataError
from database.factories import UserFactory, FileFactory, FileDetailFactory
from database.models.setting import Session


class FileService():

    def __init__(self, file: tp.Type[ApiFile]):

        self.file = file

    def save_file(self) -> dict:

        try:
            session = Session()

            user = UserFactory.build(name=self.file.user_name)
            file = FileFactory.build(users=user, name=self.file.name)
            session.add(user)
            session.add(file)
            for detail in self.file.details:
                session.add(FileDetailFactory.build(files=file,
                                                    row=detail.row,
                                                    contents=detail.contents))

            session.commit()

            result = {'message': 'Success'}
        except DataError:
            raise DataBaseDataError
        except SQLAlchemyError:
            raise DataBaseConnecitonError

        return result
