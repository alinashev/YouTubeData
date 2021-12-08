import logging
from datetime import datetime

from Action.Action import Action
from Settings import settings
from Tables.TableCreator import TableCreator


class DBStructureCreator(Action):
    def execute(self) -> None:
        time: datetime = datetime.utcnow()
        log_file_name: str = settings.log_file_name.format(year=time.year,
                                                           month=time.month,
                                                           day=time.day,
                                                           hour=time.hour,
                                                           minute=time.minute,
                                                           second=time.second)

        logging.basicConfig(level=logging.INFO, filename=log_file_name, filemode='w',
                            format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

        table_creator = TableCreator()
        table_creator.create_all_tables('SQLCode/channel.sql')
        table_creator.create_all_tables('SQLCode/videodata.sql')
        table_creator.create_all_tables('SQLCode/videocategory .sql')


