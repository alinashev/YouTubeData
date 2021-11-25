import boto3
import settings


class StorageS3:
    __path = None
    __bucket_name = 'task-bucket-a'
    __s3 = boto3.resource('s3',
                          aws_access_key_id=settings.aws_access_key_id,
                          aws_secret_access_key=settings.aws_secret_access_key)

    def load_file_to_s3(self, log_file_name):
        self.__s3.meta.client.upload_file(log_file_name, self.__bucket_name,
                                          'Resources/Lake/jsonTypesFile/YouTube/{name}'.format(name=log_file_name))
