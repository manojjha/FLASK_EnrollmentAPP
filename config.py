import os
from posix import environ

class Config(object):
    SECRET_KY = os.environ.get('SECRET_KEY') or "seret_string"