import psycopg2
from psycopg2.extras import RealDictCursor
from ..Config import settings

import time


class Database:

    def connection(self):
        while True:
            try:

                conn = psycopg2.connect(host=settings.host, database=settings.db_name, user=settings.db_user_name,
                                        password=settings.db_password, cursor_factory=RealDictCursor )

                print("connected")
                break
            except Exception as error:
                print("connection faild")
                print(error)
                time.sleep(2)
        return conn
database=Database()