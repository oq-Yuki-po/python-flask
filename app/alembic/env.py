from logging.config import fileConfig
import logging

from sqlalchemy import create_engine
from sqlalchemy import pool
from sqlalchemy_utils import database_exists, create_database

from alembic import context

from config import BaseConfig
from database.models.setting import BaseModel, initialize_db

# this is the Alembic Config object, which provides
# access to the values within the .ini file in use.
config = context.config

# Interpret the config file for Python logging.
# This line sets up loggers basically.
fileConfig(config.config_file_name)

# add your model's MetaData object here
# for 'autogenerate' support
target_metadata = BaseModel.metadata

# other values from the config, defined by the needs of env.py,
# can be acquired:
# my_important_option = config.get_main_option("my_important_option")
# ... etc.


def run_migrations_offline():
    """Run migrations in 'offline' mode.

    This configures the context with just a URL
    and not an Engine, though an Engine is acceptable
    here as well.  By skipping the Engine creation
    we don't even need a DBAPI to be available.

    Calls to context.execute() here emit the given string to the
    script output.

    """
    url = BaseConfig.DATABASE
    context.configure(
        url=url, target_metadata=target_metadata, literal_binds=True)

    with context.begin_transaction():
        context.run_migrations()


def run_migrations_online():
    """Run migrations in 'online' mode.

    In this scenario we need to create an Engine
    and associate a connection with the context.

    """
    url = BaseConfig.DATABASE
    connectable = create_engine(url)

    with connectable.connect() as connection:
        context.configure(
            url=url,
            connection=connection,
            target_metadata=target_metadata
        )

        with context.begin_transaction():
            context.run_migrations()


initialize_db()

if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()
