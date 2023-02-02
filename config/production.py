from config.default import *

SQLALCHEMY_DATABASE_URI = f'sqlite:///{os.path.join(BASE_DIR, "pybo.db")}'
SQLALCEHMY_TRACK_MODIFICATIONS = False
SECRET_KEY = b'[*pf\x81)\xbd\xbb\x16pL\xe2\xd5\xfd\x17\xee'