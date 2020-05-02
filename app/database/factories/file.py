from datetime import datetime

import factory
from factory.alchemy import SQLAlchemyModelFactory

from database.models import Session, File
from database.factories import UserFactory


class FileFactory(SQLAlchemyModelFactory):
    class Meta:

        model = File

        sqlalchemy_session = Session

        sqlalchemy_session_persistence = 'commit'

    name = factory.Faker('file_name', extension='txt')
    users = factory.SubFactory(UserFactory)
    created_at = datetime.now()
    updated_at = datetime.now()
