import os
import boto3
import settings


class StorageS3:
    __path = None
    __bucket_name = 'task-bucket-a'
    __s3 = boto3.resource('s3',
                          aws_access_key_id=settings.aws_access_key_id,
                          aws_secret_access_key=settings.aws_secret_access_key)

    def download_folder(self, destination_directory):
        bucket = self.__s3.Bucket(self.__bucket_name)
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

    @staticmethod
    def get_path_list(directory):
        os.chdir(directory)
        return [os.path.join(root, name) for root, dirs, files in os.walk(".", topdown=False) for name in files]

    def load_file_to_s3(self, file_name):
        self.__s3.meta.client.upload_file(file_name, self.__bucket_name,
                                          'Resources/Lake/jsonTypesFile/YouTube/{name}'.format(name=file_name))
