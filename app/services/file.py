import typing as tp

from sqlalchemy.exc import SQLAlchemyError, DBAPIError
from api.requests.classes import File as ApiFile
from api.responses.errors import DataBaseConnecitonError, DataBaseApiError, InternalServerError
from database.models import Session, FileDetail, File, User


class FileService():

    def __init__(self, file: tp.Type[ApiFile]):

        self.file = file

    def save_file(self) -> dict:

        try:
            session = Session()

            user = User(name=self.file.user_name)

            file = File(user=user, name=self.file.name)

            session.add(user)
            session.add(file)

            session.flush()

            details = [{'row': d.row, 'contents': d.contents, 'file_id': file.id} for d in self.file.details]
            session.execute(FileDetail.__table__.insert(), details)

            session.commit()

            result = {'message': 'Success'}
        except DBAPIError:
            raise DataBaseApiError
        except SQLAlchemyError:
            raise DataBaseConnecitonError
        except Exception:
            raise InternalServerError
        finally:
            session.close()

        return result
