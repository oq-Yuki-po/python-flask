import pytest

from database.models import User, File, FileDetail
from api_requests.factories import FileFactory, FileDetailFactory


@pytest.mark.usefixtures('create_all_tables')
class TestFilesApi():

    def test_post(self, app_client, count_records):
        file_details = FileDetailFactory.build_batch(10)
        payload = FileFactory(details=file_details).to_json(ensure_ascii=False)

        response = app_client.post('/files',
                                   data=payload)

        assert response.status_code == 200
        assert count_records(User) == 1
        assert count_records(File) == 1
        assert count_records(FileDetail) == 10
