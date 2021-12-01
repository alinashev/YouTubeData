import logging
import os
from typing import Any

import boto3
import settings


class StorageS3:
    __path: str
    __bucket_name: str = 'task-bucket-a'
    __s3: Any = boto3.resource('s3',
                               aws_access_key_id=settings.aws_access_key_id,
                               aws_secret_access_key=settings.aws_secret_access_key)
    __downloaded_directory: str

    def download_folder(self, destination_directory: str) -> None:
        self.__downloaded_directory = destination_directory
        bucket: Any = self.__s3.Bucket(self.__bucket_name)
        for obj in bucket.objects.filter(Prefix='Resources'):
            if destination_directory is False:
                self.__path = obj.key
            else:
                self.__path = os.path.join(destination_directory, os.path.relpath(obj.key, 'Resources'))
            if os.path.exists(os.path.dirname(self.__path)) is False:
                os.makedirs(os.path.dirname(self.__path))
            if obj.key[-1] == '/':
                continue
            bucket.download_file(obj.key, self.__path)
            logging.info("Data downloaded from S3")
        self.__downloaded_directory = destination_directory

    def get_downloaded_directory(self) -> str:
        return self.__downloaded_directory

    def get_path_list(self) -> list[str]:
        directory = self.get_downloaded_directory()
        os.chdir(directory)
        path_list = list()
        for root, dirs, files in os.walk(".", topdown=False):
            for name in files:
                path_list.append(os.path.join(root, name))
        return path_list

    def upload(self, file_name: str) -> None:
        self.__s3.meta.client.upload_file(file_name, self.__bucket_name,
                                          'Resources/Lake/jsonTypesFile/YouTube/{name}'.format(name=file_name))
        logging.info("Pulled data has been loaded into S3")