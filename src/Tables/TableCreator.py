import logging
from typing import Any

from Commons.DataBase import DataBase


class TableCreator:
    def create_all_tables(self, file):
        try:
            data_base: DataBase = DataBase()
            connect: Any = data_base.connect()
            cursor: Any = connect.cursor()

            sql_file = open(file, 'r')
            cursor.execute(sql_file.read())
            connect.commit()

            logging.info('Successfully created')
            data_base.close()
        except Exception as error:
            logging.error(error)
