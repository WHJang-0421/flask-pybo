from config.default import *
from logging.config import dictConfig
from dotenv import load_dotenv

load_dotenv(os.path.join(BASE_DIR, '.env'))

SQLALCHEMY_DATABASE_URI = f'postgresql+psycopg2://{os.getenv("DB_USER")}:{os.getenv("DB_PASSWORD")}@{os.getenv("DB_HOST")/{os.getenv("DB_NAME")}}'
SQLALCEHMY_TRACK_MODIFICATIONS = False
SECRET_KEY = b'[*pf\x81)\xbd\xbb\x16pL\xe2\xd5\xfd\x17\xee'

dictConfig({
    'version': 1,
    'formatters': {
        'default': {
            'format': '[%(asctime)s] %(levelname)s in %(module)s: %(message)s',
        },
    },
    'handlers': {
        'file': {
            'level': 'INFO',
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': os.path.join(BASE_DIR, 'logs/flask-pybo.log'),
            'maxBytes': 1024 * 1024 * 5, # 5MB
            'backupCount': 5,
            'formatter': 'default',
        },
    },
    'root': {
        'level': 'INFO',
        'handlers': ['file'],
    },
})