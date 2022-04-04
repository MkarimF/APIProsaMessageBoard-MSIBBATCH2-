from sqlalchemy import engine_from_config
import post.database as _database
import post.models as _models


def _add_tables():
    return _database.Base.metadata.create_all(bind=_database.engine)