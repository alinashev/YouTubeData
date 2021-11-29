import logging
from typing import Any

import psycopg2
from psycopg2 import Error
import settings


class DataBase:
    __connection: None = None

    __user: str = settings.rds_user
    __password: str = settings.rds_password
    __database: str = settings.rds_database
    __host: str = settings.rds_host
    __port: str = settings.rds_port

    @classmethod
    def connect(cls) -> Any:
        if not cls.__connection:
            logging.info('Establishing connection...')
            try:
                cls.__connection = psycopg2.connect(user=cls.__user,
                                                    password=cls.__password,
                                                    database=cls.__database,
                                                    host=cls.__host,
                                                    port=cls.__port)
            except (Exception, Error) as error:
                logging.error(error)

        else:
            logging.info('Connection established')
        return cls.__connection

    @classmethod
    def close(cls) -> None:
        try:
            if cls.__connection:
                logging.info('Close connection')
                cls.__connection.close()
        except (Exception, Error) as error:
            logging.error(error)
