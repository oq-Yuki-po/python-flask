import os

from sqlalchemy.schema import CreateSchema, DropSchema
from sqlalchemy_utils import database_exists, create_database
from flask.testing import FlaskClient
import pytest

from main import app
from database.models.setting import Engine, DB_Base, Session


class CustomClient(FlaskClient):
    def open(self, *args, **kwargs):
        kwargs.setdefault('content_type', 'application/json')
        return super().open(*args, **kwargs)


@pytest.fixture(scope='session', autouse=True)
def create_test_environment(request):

    if not database_exists(Engine.url):
        create_database(Engine.url)

    schema_name = os.environ.get('DB_SCHEMA', "test")

    if not Engine.dialect.has_schema(Engine, schema_name):
        Engine.execute(CreateSchema(schema_name))

    def drop_schema():
        Engine.execute(DropSchema(schema_name))

    request.addfinalizer(drop_schema)

    return create_test_environment


@pytest.fixture()
def create_all_tables(request):
    DB_Base.metadata.create_all(Engine)

    def drop_all_tables():
        DB_Base.metadata.drop_all(Engine)

    request.addfinalizer(drop_all_tables)

    return create_all_tables


@pytest.fixture(autouse=True)
def app_client():
    app.test_client_class = CustomClient
    with app.test_client() as client:
        with app.app_context():
            yield client

@pytest.fixture()
def count_records():
    def _count_records(model):
        session = Session()
        count = session.query(model).count()
        session.close()
        return count
    return _count_records
