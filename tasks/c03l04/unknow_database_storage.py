from icecream import ic
from sqlalchemy import create_engine, Column, String, Date
from sqlalchemy.orm import sessionmaker, declarative_base
import psycopg2
import uuid

Base = declarative_base()

CONNECTION_STRING = 'postgresql://postgres:postgres@127.0.0.1:5432/unknow_news'


class UnknowNews(Base):
    __tablename__ = 'unknow_news'

    id = Column(String, primary_key=True, default=str(uuid.uuid4()))
    title = Column(String)
    url = Column(String)
    info = Column(String)
    date = Column(Date)


def create_postgresql_session():
    engine = create_engine(CONNECTION_STRING)
    Session = sessionmaker(bind=engine)
    return Session()


def create_tables():
    engine = create_engine(CONNECTION_STRING)
    Base.metadata.create_all(engine)  # run only once


def delete_sql_data():
    # delete all rows in the User table
    session = create_postgresql_session()
    session.query(UnknowNews).delete()
    # commit the transaction
    session.commit()


def test_insert():
    session = create_postgresql_session()
    info_id = str(uuid.uuid4())
    ic(info_id)

    count = session.query(UnknowNews).count()
    ic(count)

    news = UnknowNews(id=info_id, title='Title', url='https://example.com', info='Information', date='2023-11-12')
    session.add(news)
    session.commit()

    count = session.query(UnknowNews).count()
    ic(count)

    news_to_delete = session.query(UnknowNews).filter_by(id=info_id).first()
    ic(news_to_delete.id)
    session.delete(news_to_delete)
    session.commit()

    count = session.query(UnknowNews).count()
    ic(count)


if __name__ == "__main__":
    test_insert()
