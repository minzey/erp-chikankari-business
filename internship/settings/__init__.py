from .base import *

environment = os.environ.get("taanabaana_environment", "dev")

if environment == "prod":
    from .production import *
