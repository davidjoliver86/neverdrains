# pylint: disable=wildcard-import,unused-wildcard-import
# "Dev" is effectively "Local".


import os
from dotenv import load_dotenv
from .settings import *


load_dotenv()

SECRET_KEY = os.environ["SECRET_KEY"]

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": "neverdrains",
        "HOST": "127.0.0.1",
        "PORT": 5432,
        "USER": os.environ["DB_USER"],
        "PASSWORD": os.environ["DB_PASSWORD"],
    }
}
