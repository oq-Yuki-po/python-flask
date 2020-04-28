import factory

from api_requests.classes import File
from api_requests.factories import FileDetailFactory


class FileFactory(factory.Factory):
    class Meta:

        model = File

    name = factory.Faker('file_name', extension='txt')
    user_name = factory.Faker('user_name', locale='ja_JP')
    details = factory.List(
        [factory.SubFactory(FileDetailFactory) for _ in range(5)])
