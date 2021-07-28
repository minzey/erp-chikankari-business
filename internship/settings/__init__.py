from .base import *

environment = os.environ.get("taanabaana_environment", "dev")
print(f"CURRENT ENVIRONMENT: {environment}")
if environment == "prod":
    from .production import *
