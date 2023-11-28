from alembic import context
from sqlalchemy import engine_from_config, pool

# Add the path to your project directory
import os
import sys

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from models.model import db, UserAccount, Mobile, Review, Question

# Use the same database URL as specified in alembic.ini
config = context.config
config.set_main_option('sqlalchemy.url', 'postgresql+psycopg2://postgres:Nani8901@database-staging.cq5odtnxninx.us-east-1.rds.amazonaws.com/MyDataBase')

# Define target_metadata
target_metadata = db.metadata

# this callback is used to prevent an error in alembic's revision history table
def include_schemas():
    return True

def run_migrations_online():
    engine = engine_from_config(
        config.get_section(config.config_ini_section),
        prefix='sqlalchemy.',
        poolclass=pool.NullPool,
    )

    connection = engine.connect()
    context.configure(
        target_metadata=target_metadata,  # Set the target_metadata
        connection=connection,
        compare_type=True,
    )

    try:
        with context.begin_transaction():
            context.run_migrations()
    finally:
        connection.close()

run_migrations_online()
