from .config import Config
from .database import Database
from .cache import Cache
from .embed import Embed

from .errors import (ModuleDisabled, CommandDisabled)

Config = Config()
db = Database()
Cache = Cache()
