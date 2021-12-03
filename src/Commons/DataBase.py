import logging
from typing import Any

import psycopg2
from psycopg2 import Error

from Settings import databaseSettings


class DataBase:
    def __init__(self) -> None:
        self.__connection = None

    def connect(self, user=databaseSettings.user, password=databaseSettings.password,
                database=databaseSettings.database, host=databaseSettings.host, port=databaseSettings.port) -> Any:
        if not self.__connection:
            logging.info('Establishing connection...')
            try:
                self.__connection = psycopg2.connect(user=user,
                                                     password=password,
                                                     database=database,
                                                     host=host,
                                                     port=port)
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