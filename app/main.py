from flask_restful import Api
from database.models.setting import initialize_db
from controllers import initialize_routes
from setup import make_flask_app, before_request, after_request, set_logger
from api.responses.errors import Errors

app = make_flask_app(__name__)

api = Api(app, errors=Errors, catch_all_404s=True, prefix=app.config.get('API_VERSION'))

set_logger(app)

initialize_db()

initialize_routes(api)

app.before_request(before_request)

app.after_request(after_request)

if __name__ == '__main__':
    app.run()
