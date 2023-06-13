from data_models.database import Base,engine, get_db
import data_models.crud as crud

Base.metadata.create_all(bind= engine)

db_session = next(get_db())
