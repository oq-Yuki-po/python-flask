import factory

from api_requests.classes import FileDetail


class FileDetailFactory(factory.Factory):
    class Meta:

        model = FileDetail

    row = factory.Sequence(lambda n: n+1)
    contents = factory.Faker('text', max_nb_chars=5, locale='ja_JP')
