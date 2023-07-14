import os
import logging

basedir = os.path.abspath(os.path.join(os.path.dirname(__file__),"."))


class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'MYSECRET'
    SITE_NAME = 'SYSTEMDB'
    SITE_ROOT_URL = 'http://127.0.0.1:8000'
    LOG_LEVEL = logging.DEBUG
    DEBUG=True

    # 200 MB
    MAX_CONTENT_LENGTH = 1024 * 1024 * 200
    UPLOAD_EXTENSIONS = ['.xml']
    UPLOAD_DIR = os.path.abspath(os.path.join(basedir, os.pardir))+ "/uploads/"

    LANGUAGES = ['en', 'de']

    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'sqlite:///' + os.path.join(basedir, 'systemdb.sqlite')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_RECORD_QUERIES = True

    # Enable protection agains *Cross-site Request Forgery (CSRF)*
    CSRF_ENABLED = True
    CSRF_SESSION_KEY = "secret"

    TEMPLATES_AUTO_RELOAD = True

    # API settings
    API_TITLE = "SYSTEMDB API"
    API_VERSION = "v0.3"
    API_ENABLED = False
    OPENAPI_VERSION = "3.0.2"
    OPENAPI_JSON_PATH = "api-spec.json"
    OPENAPI_URL_PREFIX = "/"
    OPENAPI_REDOC_PATH = "/redoc"
    OPENAPI_REDOC_URL = (
        "https://cdn.jsdelivr.net/npm/redoc@next/bundles/redoc.standalone.js"
    )
    OPENAPI_SWAGGER_UI_PATH = "/swagger-ui"
    OPENAPI_SWAGGER_UI_URL = "https://cdn.jsdelivr.net/npm/swagger-ui-dist/"
    OPENAPI_RAPIDOC_PATH = "/rapidoc"
    OPENAPI_RAPIDOC_URL = "https://unpkg.com/rapidoc/dist/rapidoc-min.js"
