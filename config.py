import os

SECRET_KEY = '861b1dabae5b0c120887061e55b958a4acbd2cd5850b66412f6e38cec69b0e93'

MYSQL_USER = 'root'
MYSQL_PASSWORD = 'Qwerty_123'
MYSQL_HOST = 'mysql'
MYSQL_DATABASE = 'sys'

ADMIN_ROLE_ID = 1
MODER_ROLE_ID = 2
USER_ROLE_ID = 3

UPLOAD_FOLDER = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'media/images')