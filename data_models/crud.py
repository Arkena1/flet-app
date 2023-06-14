from sqlalchemy.orm import Session
import data_models.dbmodels as model
import data_models.schemas as schemas
# Province# Province# Province# Province# Province# Province# Province# Province# Province# Province

def create_province(db: Session, data: schemas.Province):
    "Создание провинции "
    db_data = model.Province(**data)
    db.add(db_data)
    db.commit()
    db.refresh(db_data)
    return db_data

def delete_province(db: Session, id: int):
    ss = db.query(model.Province).filter(model.Province.id == id)
    ss.delete(synchronize_session=False)
    db.commit()
    return {"msg": f"Удаление провинции с {id=} завершено"}

def update_province(db: Session, data: schemas.Province):
    loc_model = model.Province(**data)
    ss = db.query(model.Province).filter(model.Province.id == loc_model.id)
    ss.update(data)
    db.commit()
    return model

def get_provinces(db: Session):
    """Получение всех данных провинции"""
    ss = db.query(model.Province)
    result = [schemas.Province(**data.__dict__).dict() for data in ss.all()]
    return result

def get_province(db: Session, id: int):
    ss = db.query(model.Province).filter(model.Province.id == id)
    tt = ss.one()
    result = schemas.Province(**tt.__dict__).dict()
    return result

# Sub_province# Sub_province# Sub_province# Sub_province# Sub_province# Sub_province# Sub_province

def create_sub_province(db: Session, data: schemas.SubProvince): 
    db_data = model.SubProvince(**data)
    db.add(db_data)
    db.commit()
    db.refresh(db_data)
    return db_data

def delete_sub_province(db: Session, id: int):
    ss = db.query(model.SubProvince).filter(model.SubProvince.id == id)
    ss.delete(synchronize_session=False)
    db.commit()
    return {"msg": f"Удаление субпровинции с {id=} завершено"}

def update_sub_province(db: Session, data: schemas.SubProvince):
    loc_model = model.SubProvince(**data)
    ss = db.query(model.SubProvince).filter(model.SubProvince.id == loc_model.id)
    ss.update(data)
    db.commit()
    return model

def get_sub_provinces(db: Session):
    ss = db.query(model.SubProvince)
    result = [schemas.SubProvince(**data.__dict__).dict() for data in ss.all()]
    return result

def get_sub_province(db: Session, id: int):
    ss = db.query(model.SubProvince).filter(model.SubProvince.id == id)
    tt = ss.one()
    result = schemas.SubProvince(**tt.__dict__).dict()
    return result

# Area# Area# Area# Area# Area# Area# Area# Area# Area# Area# Area# Area# Area# Area# Area

def create_area(db: Session, data: schemas.Area): 
    db_data = model.Area(**data)
    db.add(db_data)
    db.commit()
    db.refresh(db_data)
    return db_data

def delete_area(db: Session, id: int):
    ss = db.query(model.Area).filter(model.Area.id == id)
    ss.delete(synchronize_session=False)
    db.commit()
    return {"msg": f"Удаление района с {id=} завершено"}

def update_area(db: Session, data: schemas.Area):
    loc_model = model.Area(**data)
    ss = db.query(model.Area).filter(model.Area.id == loc_model.id)
    ss.update(data)
    db.commit()
    return model

def get_areas(db: Session):
    ss = db.query(model.Area)
    result = [schemas.Area(**data.__dict__).dict() for data in ss.all()]
    return result

def get_area(db: Session, id: int):
    ss = db.query(model.Area).filter(model.Area.id == id)
    tt = ss.one()
    result = schemas.Area(**tt.__dict__).dict()
    return result

# Field# Field# Field# Field# Field# Field# Field# Field# Field# Field# Field# Field# Field

def create_field(db: Session, data: schemas.Field): 
    db_data = model.Field(**data)
    db.add(db_data)
    db.commit()
    db.refresh(db_data)
    return db_data

def delete_field(db: Session, id: int):
    ss = db.query(model.Field).filter(model.Field.id == id)
    ss.delete(synchronize_session=False)
    db.commit()
    return {"msg": f"Удаление поля с {id=} завершено"}

def update_field(db: Session, data: schemas.Field):
    loc_model = model.Field(**data)
    ss = db.query(model.Field).filter(model.Field.id == loc_model.id)
    ss.update(data)
    db.commit()
    return model

def get_fields(db: Session):
    ss = db.query(model.Field)
    result = [schemas.AField(**data.__dict__).dict() for data in ss.all()]
    return result

def get_field(db: Session, id: int):
    ss = db.query(model.Field).filter(model.Field.id == id)
    tt = ss.one()
    result = schemas.Field(**tt.__dict__).dict()
    return result

# Pipe# Pipe# Pipe# Pipe# Pipe# Pipe# Pipe# Pipe# Pipe# Pipe# Pipe# Pipe# Pipe# Pipe# Pipe

def create_pipe(db: Session, data: schemas.Pipe): 
    db_data = model.Pipe(**data)
    db.add(db_data)
    db.commit()
    db.refresh(db_data)
    return db_data

def delete_pipe(db: Session, id: int):
    ss = db.query(model.Pipe).filter(model.Pipe.id == id)
    ss.delete(synchronize_session=False)
    db.commit()
    return {"msg": f"Удаление трубки с {id=} завершено"}

def update_pipe(db: Session, data: schemas.Pipe):
    loc_model = model.Pipe(**data)
    ss = db.query(model.Pipe).filter(model.Pipe.id == loc_model.id)
    ss.update(data)
    db.commit()
    return model

def get_pipes(db: Session):
    ss = db.query(model.Pipe)
    result = [schemas.Pipe(**data.__dict__).dict() for data in ss.all()]
    return result

def get_pipe(db: Session, id: int):
    ss = db.query(model.Pipe).filter(model.Pipe.id == id)
    tt = ss.one()
    result = schemas.Pipe(**tt.__dict__).dict()
    return result

# Sours# Sours# Sours# Sours# Sours# Sours# Sours# Sours# Sours# Sours# Sours# Sours# Sours

def create_source(db: Session, data: schemas.Source): 
    db_data = model.Source(**data)
    db.add(db_data)
    db.commit()
    db.refresh(db_data)
    return db_data

def delete_source(db: Session, id: int):
    ss = db.query(model.Source).filter(model.Source.id == id)
    ss.delete(synchronize_session=False)
    db.commit()
    return {"msg": f"Удаление трубки с {id=} завершено"}

def update_source(db: Session, data: schemas.Source):
    loc_model = model.Source(**data)
    ss = db.query(model.Source).filter(model.Source.id == loc_model.id)
    ss.update(data)
    db.commit()
    return model

def get_sources(db: Session):
    ss = db.query(model.Source)
    result = [schemas.Source(**data.__dict__).dict() for data in ss.all()]
    return result

def get_source(db: Session, id: int):
    ss = db.query(model.Source).filter(model.Source.id == id)
    tt = ss.one()
    result = schemas.Source(**tt.__dict__).dict()
    return result

# Pipeinfo# Pipeinfo# Pipeinfo# Pipeinfo# Pipeinfo# Pipeinfo# Pipeinfo# Pipeinfo# Pipeinfo

def create_pipeinfo(db: Session, data: schemas.Pipeinfo): 
    db_data = model.Pipeinfo(**data)
    db.add(db_data)
    db.commit()
    db.refresh(db_data)
    return db_data

def delete_pipeinfo(db: Session, id: int):
    ss = db.query(model.Pipeinfo).filter(model.Pipeinfo.id == id)
    ss.delete(synchronize_session=False)
    db.commit()
    return {"msg": f"Удаление трубки с {id=} завершено"}

def update_pipeinfo(db: Session, data: schemas.Pipeinfo):
    loc_model = model.Pipeinfo(**data)
    ss = db.query(model.Pipeinfo).filter(model.Pipeinfo.id == loc_model.id)
    ss.update(data)
    db.commit()
    return model

def get_pipeinfos(db: Session):
    ss = db.query(model.Pipeinfo)
    result = [schemas.Pipeinfo(**data.__dict__).dict() for data in ss.all()]
    return result

def get_pipeinfo(db: Session, id: int):
    ss = db.query(model.Pipeinfo).filter(model.Pipeinfo.id == id)
    tt = ss.one()
    result = schemas.Pipeinfo(**tt.__dict__).dict()
    return result
