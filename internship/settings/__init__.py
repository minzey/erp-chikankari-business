from .base import *

environment = os.environ.get("taanabaana_environment", "dev")
print(environment)
from .production import *
