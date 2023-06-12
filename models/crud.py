import models
import schemas
from sqlalchemy.orm import Session

# Province# Province# Province# Province# Province# Province# Province# Province# Province# Province

def create_province(db: Session, data: schemas.Province):
    db_data = models.Province(**data)
    db.add(db_data)
    db.commit()
    db.refresh(db_data)
    return db_data

def delete_provinces(db:Session, id:int ):
    ss = db.query(models.Province).filter(models.Province.id == id)
    ss.delete(synchronize_session=False)
    db.commit()
    return {"msg": f"Удаление провинции с {id=} завершено"}

def update_provinces(db:Session, data: schemas.Province ):
    model = models.Province(**data)
    ss = db.query(models.Province).filter(models.Province.id == model.id)
    ss.update(data)
    db.commit()
    return model

def get_provinces(db: Session):
    ss = db.query(models.Province)
    result = [schemas.Province(**data.__dict__) for data in ss.all()]
    return result

def get_province(db: Session, id: int):
    ss = db.query(models.Province).filter(models.Province.id == id)
    tt = ss.one()
    result = schemas.Province(**tt.__dict__)
    return result

# Sub_province# Sub_province# Sub_province# Sub_province# Sub_province# Sub_province# Sub_province

def create_sub_province(db: Session, data: schemas.SubProvince): 
    db_data = models.SubProvince(**data)
    db.add(db_data)
    db.commit()
    db.refresh(db_data)
    return db_data

def delete_sub_province(db:Session, id:int ):
    ss = db.query(models.SubProvince).filter(models.SubProvince.id == id)
    ss.delete(synchronize_session=False)
    db.commit()
    return {"msg": f"Удаление субпровинции с {id=} завершено"}

def update_sub_province(db:Session, data: schemas.SubProvince ):
    model = models.SubProvince(**data)
    ss = db.query(models.SubProvince).filter(models.SubProvince.id == model.id)
    ss.update(data)
    db.commit()
    return model

def get_sub_province(db: Session):
    ss = db.query(models.SubProvince)
    result = [schemas.SubProvince(**data.__dict__) for data in ss.all()]
    return result

def get_sub_province(db: Session, id: int):
    ss = db.query(models.SubProvince).filter(models.SubProvince.id == id)
    tt = ss.one()
    result = schemas.SubProvince(**tt.__dict__)
    return result

# Area# Area# Area# Area# Area# Area# Area# Area# Area# Area# Area# Area# Area# Area# Area

def create_area(db: Session, data: schemas.area): 
    db_data = models.Area(**data)
    db.add(db_data)
    db.commit()
    db.refresh(db_data)
    return db_data

def delete_area(db:Session, id:int ):
    ss = db.query(models.Area).filter(models.Area.id == id)
    ss.delete(synchronize_session=False)
    db.commit()
    return {"msg": f"Удаление района с {id=} завершено"}

def update_area(db:Session, data: schemas.Area ):
    model = models.Area(**data)
    ss = db.query(models.Area).filter(models.Area.id == model.id)
    ss.update(data)
    db.commit()
    return model

def get_area(db: Session):
    ss = db.query(models.Area)
    result = [schemas.Area(**data.__dict__) for data in ss.all()]
    return result

def get_area(db: Session, id: int):
    ss = db.query(models.Area).filter(models.Area.id == id)
    tt = ss.one()
    result = schemas.Area(**tt.__dict__)
    return result

# Field# Field# Field# Field# Field# Field# Field# Field# Field# Field# Field# Field# Field

def create_field(db: Session, data: schemas.Field): 
    db_data = models.Field(**data)
    db.add(db_data)
    db.commit()
    db.refresh(db_data)
    return db_data

def delete_field(db:Session, id:int ):
    ss = db.query(models.Field).filter(models.Field.id == id)
    ss.delete(synchronize_session=False)
    db.commit()
    return {"msg": f"Удаление поля с {id=} завершено"}

def update_field(db:Session, data: schemas.Field ):
    model = models.Field(**data)
    ss = db.query(models.Field).filter(models.Field.id == model.id)
    ss.update(data)
    db.commit()
    return model

def get_field(db: Session):
    ss = db.query(models.Field)
    result = [schemas.AField(**data.__dict__) for data in ss.all()]
    return result

def get_field(db: Session, id: int):
    ss = db.query(models.Field).filter(models.Field.id == id)
    tt = ss.one()
    result = schemas.Field(**tt.__dict__)
    return result

# Pipe# Pipe# Pipe# Pipe# Pipe# Pipe# Pipe# Pipe# Pipe# Pipe# Pipe# Pipe# Pipe# Pipe# Pipe

def create_pipe(db: Session, data: schemas.Pipe): 
    db_data = models.Pipe(**data)
    db.add(db_data)
    db.commit()
    db.refresh(db_data)
    return db_data

def delete_pipe(db:Session, id:int ):
    ss = db.query(models.Pipe).filter(models.Pipe.id == id)
    ss.delete(synchronize_session=False)
    db.commit()
    return {"msg": f"Удаление трубки с {id=} завершено"}

def update_pipe(db:Session, data: schemas.Pipe ):
    model = models.Pipe(**data)
    ss = db.query(models.Pipe).filter(models.Pipe.id == model.id)
    ss.update(data)
    db.commit()
    return model

def get_pipe(db: Session):
    ss = db.query(models.Pipe)
    result = [schemas.Pipe(**data.__dict__) for data in ss.all()]
    return result

def get_pipe(db: Session, id: int):
    ss = db.query(models.Pipe).filter(models.Pipe.id == id)
    tt = ss.one()
    result = schemas.Pipe(**tt.__dict__)
    return result

# Sours# Sours# Sours# Sours# Sours# Sours# Sours# Sours# Sours# Sours# Sours# Sours# Sours

def create_sours(db: Session, data: schemas.Sours): 
    db_data = models.Sours(**data)
    db.add(db_data)
    db.commit()
    db.refresh(db_data)
    return db_data

def delete_sours(db:Session, id:int ):
    ss = db.query(models.Sours).filter(models.Sours.id == id)
    ss.delete(synchronize_session=False)
    db.commit()
    return {"msg": f"Удаление трубки с {id=} завершено"}

def update_sours(db:Session, data: schemas.Sours ):
    model = models.Sours(**data)
    ss = db.query(models.Sours).filter(models.Sours.id == model.id)
    ss.update(data)
    db.commit()
    return model

def get_sours(db: Session):
    ss = db.query(models.Sours)
    result = [schemas.Sours(**data.__dict__) for data in ss.all()]
    return result

def get_sours(db: Session, id: int):
    ss = db.query(models.Sours).filter(models.Sours.id == id)
    tt = ss.one()
    result = schemas.Sours(**tt.__dict__)
    return result