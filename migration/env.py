from logging.config import fileConfig

from sqlalchemy import engine_from_config
from sqlalchemy import pool
import sys
from os.path import abspath, dirname
from alembic import context



sys.path.insert(0, dirname(dirname(dirname(abspath(__file__)))))

from app.config import settings
from app.database import Base
from app.models.accommodations.model import Accommodations
from app.models.accommodations_usage.model import Accommodations_usage
from app.models.bookings.models import Bookings
from app.models.clients.models import Clients
from app.models.procedure_appointment.models import Procedure_appointment
from app.models.procedures.models import Procedures
from app.models.room_usage.models import Room_usage
from app.models.rooms.models import Rooms
from app.models.staff.models import Staff
from app.models.room_status.models import RoomStatus


# this is the Alembic Config object, which provides
# access to the values within the .ini file in use.
config = context.config

config.set_main_option("sqlalchemy.url", f"{settings.DB_URL}?async_fallback=True")

# Interpret the config file for Python logging.
# This line sets up loggers basically.
if config.config_file_name is not None:
    fileConfig(config.config_file_name)

# add your model's MetaData object here
# for 'autogenerate' support
# from myapp import mymodel
# target_metadata = mymodel.Base.metadata
target_metadata = Base.metadata

# other values from the config, defined by the needs of env.py,
# can be acquired:
# my_important_option = config.get_main_option("my_important_option")
# ... etc.


def run_migrations_offline() -> None:
    """Run migrations in 'offline' mode.

    This configures the context with just a URL
    and not an Engine, though an Engine is acceptable
    here as well.  By skipping the Engine creation
    we don't even need a DBAPI to be available.

    Calls to context.execute() here emit the given string to the
    script output.

    """
    url = config.get_main_option("sqlalchemy.url")
    context.configure(
        url=url,
        target_metadata=target_metadata,
        literal_binds=True,
        dialect_opts={"paramstyle": "named"},
    )

    with context.begin_transaction():
        context.run_migrations()


def run_migrations_online() -> None:
    """Run migrations in 'online' mode.

    In this scenario we need to create an Engine
    and associate a connection with the context.

    """
    connectable = engine_from_config(
        config.get_section(config.config_ini_section, {}),
        prefix="sqlalchemy.",
        poolclass=pool.NullPool,
    )

    with connectable.connect() as connection:
        context.configure(
            connection=connection, target_metadata=target_metadata
        )

        with context.begin_transaction():
            context.run_migrations()


if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()
