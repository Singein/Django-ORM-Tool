import json
import os

import django

DATABASES = {
    'DATABASES': {
        'default': {
            'ENGINE': 'django.db.backends.postgresql',
            'NAME': 'xxx',
            'USER': 'postgres',
            'PASSWORD': '',
            'HOST': '',
            'PORT': '',
        }
    }
}

DEFAULT_FILENAME = 'dbconfig.json'


class DotlibError(Exception):

    def __init__(self, dbconfig_path):
        print("DBConfig file [%s] missed!" % dbconfig_path)
        with open(dbconfig_path, 'w', encoding='utf-8') as f:
            f.write(json.dumps(TEMPLATE, indent=4))
        print(
            "Dotlib has helped you create this file, please run it again after completing the information in this file")


def create_temp_config():
    """创建默认的模板配置文件
    """
    import os
    dbconfig_path = os.path.join(
        os.path.abspath(os.getcwd()), DEFAULT_FILENAME)
    with open(dbconfig_path, 'w', encoding='utf-8') as f:
        f.write(json.dumps(TEMPLATE, indent=4))


def init_context(dbconfig: str = None):
    """Django ORM module context autoloading

    Args:
        dbconfig (str):Database configuration file path, json format 
    """

    dbconfig_path = dbconfig or os.path.join(os.path.abspath(os.getcwd()),
                                             DEFAULT_FILENAME)
    if not os.path.exists(dbconfig_path):
        raise DotlibError(dbconfig_path)

    os.environ.setdefault("DOTLIB_DBCONFIG_PATH", dbconfig_path)
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "haorm.settings")
    django.setup()
    yield
