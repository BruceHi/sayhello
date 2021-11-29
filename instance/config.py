import os
import sys

from sayhello import app

# SQLite URI compatible
WIN = sys.platform.startswith('win')
if WIN:
    prefix = 'sqlite:///'
else:
    prefix = 'sqlite:////'


# 临时数据库文件 data.db 存放在 instance 下面
# 路径 D:\zufangfei\sayhello\instance
dev_db = prefix + os.path.join(app.instance_path, 'data.db')

SECRET_KEY = os.getenv('SECRET_KEY', 'secret string')
SQLALCHEMY_TRACK_MODIFICATIONS = False
SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URI', dev_db)