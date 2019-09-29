from flask_restplus import Api

from .conversion import api as migration_api


api = Api(
    version="1.0",
    title="Youtube to PDF API",
    description="An API to manage Youtube to PDF conversion",
)

api.add_namespace(migration_api, "/conversion")
