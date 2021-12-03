import logging
from typing import Any

import psycopg2
from psycopg2 import Error
import settings


class DataBase:
    def __init__(self) -> None:
        self.__connection = None

    def connect(self) -> Any:
        if not self.__connection:
            logging.info('Establishing connection...')
            try:
                self.__connection = psycopg2.connect(user=settings.rds_user,
                                                     password=settings.rds_password,
                                                     database=settings.rds_database,
                                                     host=settings.rds_host,
                                                     port=settings.rds_port)
            except (Exception, Error) as error:
                logging.error(error)

        else:
            logging.info('Connection established')
        return self.__connection

    def close(self) -> None:
        try:
            if self.__connection:
                logging.info('Close connection')
                self.__connection.close()
        except (Exception, Error) as error:
            logging.error(error)
