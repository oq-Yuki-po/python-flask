from api.route import ROUTES
from .file import FileApi


def initialize_routes(api):
    api.add_resource(FileApi, ROUTES.get('FILE').get('POST'))
