import logging
import os

from .engine import *

_ENV_VAR = "YOUTUBE_TO_PDF_SETTINGS"
_PRODUCTION = "PRODUCTION"
_DEVELOPMENT = "DEVELOPMENT"
_LOCAL = "LOCAL"

# TODO: Change whenever DEV/PROD env is needed
# if os.environ.get(_ENV_VAR) == _PRODUCTION:
#     from .production import *
# elif os.environ.get(_ENV_VAR) == _DEVELOPMENT:
#     from .development import *
if os.environ.get(_ENV_VAR) != _LOCAL:
    logging.warning("No valid value set for environment variable '{}'. "
                    "Assuming value '{}'".format(_ENV_VAR, _LOCAL))
    from .local import *
