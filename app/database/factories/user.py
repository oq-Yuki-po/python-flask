from datetime import datetime

import factory
from factory.alchemy import SQLAlchemyModelFactory

from database.models.setting import Session
from database.models import User


class UserFactory(SQLAlchemyModelFactory):
    class Meta:

        model = User

        sqlalchemy_session = Session

        sqlalchemy_session_persistence = 'commit'

    name = factory.Faker('user_name', locale='ja_JP')
    created_at = datetime.now()
    updated_at = datetime.now()
