from datetime import datetime

import factory
from factory.alchemy import SQLAlchemyModelFactory

from database.setting import session
from database.models import FileDetail
from database.factories import FileFactory


class FileDetailFactory(SQLAlchemyModelFactory):
    class Meta:

        model = FileDetail

        sqlalchemy_session = session

        sqlalchemy_session_persistence = 'commit'

    files = factory.SubFactory(FileFactory)
    row = factory.Sequence(lambda n: n+1)
    contents = factory.Faker('text', max_nb_chars=255, locale='ja_JP')
    created_at = datetime.now()
    updated_at = datetime.now()
