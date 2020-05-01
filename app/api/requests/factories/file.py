import factory

from api.requests.classes import File
from api.requests.factories import FileDetailFactory


class FileFactory(factory.Factory):
    class Meta:

        model = File

    name = factory.Faker('file_name', extension='txt')
    user_name = factory.Faker('user_name', locale='ja_JP')
    details = factory.List(
        [factory.SubFactory(FileDetailFactory) for _ in range(5)])
