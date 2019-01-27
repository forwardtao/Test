# coding: utf-8
from sqlalchemy import CHAR, Column, DECIMAL, DateTime, Float, ForeignKey, String, Table, Text, text
from sqlalchemy.dialects.mysql import BIGINT, INTEGER, MEDIUMINT, SMALLINT, TINYINT, YEAR
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
metadata = Base.metadata


class Windpy(Base):
    __tablename__ = 'windpy'

    daying = Column(DateTime, primary_key=True, server_default=text("CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP"))
    presettle = Column(DECIMAL(20, 6))
    open = Column(DECIMAL(20, 6))
    high = Column(DECIMAL(20, 6))
    low = Column(DECIMAL(20, 6))
    close = Column(DECIMAL(20, 6))
    settle = Column(DECIMAL(20, 6))

    def __repr__(self):
        return "<Host(daying='%s')>".format(self.daying)
wind = Windpy()

