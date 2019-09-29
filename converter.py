import sentry_sdk

from flask import Flask

from youtube_to_pdf import settings
from youtube_to_pdf.apis import api


app = Flask(__name__)
api.init_app(app)


@api.errorhandler
def default_error_handler(error):
    sentry_sdk.capture_exception(error)
    return {"message": "Internal Server Error"}, getattr(error, "code", 500)


if __name__ == "__main__":
    app.run(host=settings.API_HOST, port=settings.API_PORT, debug=settings.DEBUG)
