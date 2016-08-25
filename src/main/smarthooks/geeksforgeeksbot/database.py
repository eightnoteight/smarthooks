from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.exc import IntegrityError
from sqlalchemy import Column, BigInteger
from sqlalchemy import create_engine
import os

Base = declarative_base()


class Channel(Base):
    __tablename__ = 'channels'
    channel_id = Column(BigInteger, nullable=False, primary_key=True)

    def __repr__(self):
        return 'Channel(channel_id=%s)' % self.channel_id


def insert(channel_id):
    c = Channel(channel_id=channel_id)
    session.add(c)
    try:
        session.commit()
    except IntegrityError:
        # a Channel with the given channel_id already exists
        session.rollback()


def getall():
    return session.query(Channel).all()

print(os.environ['POSTGRESQL_URL'])
engine = create_engine(os.environ['POSTGRESQL_URL'])

Session = sessionmaker()
Session.configure(bind=engine)
session = Session()

Base.metadata.create_all(engine)
