from os import environ as env

import sqlalchemy as db
from sqlalchemy.orm import Session


class PostgresHandler:

    def __init__(self):
        self.engine = db.create_engine(
            f'postgresql://{env["PG_USER"]}:{env["PG_PWD"]}@{env["PG_HOST"]}/{env["PG_DB"]}'
            , echo=True)
        self.connection = self.engine.connect()
        self.metadata = db.MetaData()

    def get_engine(self):
        return self.engine

    def get_connection(self):
        return self.connection

    def get_metadata(self):
        return self.metadata

    def db_insert(self, obj_list=None):
        with Session(self.engine) as session:
            session.add_all(obj_list)
            session.commit()
