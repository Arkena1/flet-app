from sqlalchemy import String, Integer, ForeignKey, Column
from data_models.database import Base

class Province(Base):
    __tablename__ = "provinces"

    id = Column("id", Integer ,primary_key = True )
    name = Column ("name", String(255), nullable = False)

class SubProvince(Base):
    __tablename__ = "sub_provinces"

    id = Column("id", Integer ,primary_key = True )
    name = Column ("name", String(255), nullable = False)
    province_id =  Column("province_id" , ForeignKey('provinces.id'))

class Area(Base):
    __tablename__ = "areas"

    id = Column("id", Integer ,primary_key = True )
    name = Column ("name", String(255), nullable = False)
    sub_provinces_id =  Column("sub_provinces_id" , ForeignKey('sub_provinces.id'))

class Field(Base):
    __tablename__ = "fields"

    id = Column("id", Integer ,primary_key = True )
    name = Column ("name", String(255), nullable = False)
    areas_id =  Column("areas_id" , ForeignKey('areas.id'))

class Pipe(Base):
    __tablename__ = "pipes"

    id = Column("id", Integer ,primary_key = True )
    name = Column ("name", String(255), nullable = False)
    fields_id =  Column("fields_id" , ForeignKey('fields.id'))


class Source(Base):
    __tablename__ = "sources"

    id = Column("id", Integer, primary_key = True )
    name = Column ("name", String(500), nullable = False)

class PipeInfo(Base):
    __tablename__ = "pipe_info"

    id = Column("id", Integer, primary_key = True )
    nitro_total = Column ("nitro_total", String(50), nullable = True)
    nitro_a = Column ("nitro_a", String(50), nullable = True)
    nitro_b = Column ("nitro_b", String(50), nullable = True)
    nitro_percent = Column ("nitro_percent", String(50), nullable = True)
    platelets = Column ("platelets", String(50), nullable = True)
    hydrogen = Column ("hydrogen", String(50), nullable = True)
    pipes_id  = Column ("pipes_id", ForeignKey('pipes.id'))
    source_id = Column ("source_id", ForeignKey('sources.id'))
    