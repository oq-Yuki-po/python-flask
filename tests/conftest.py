import os

from sqlalchemy.schema import CreateSchema, DropSchema
from sqlalchemy_utils import database_exists, create_database
import pytest

from database.models.setting import Engine, DB_Base


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
