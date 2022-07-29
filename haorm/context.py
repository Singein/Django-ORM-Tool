import json
import os
from typing import Optional

import django

DEFAULT_SETTINGS = {
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

DEFAULT_FILENAME = 'haorm.settings.json'


class HaormSettingsError(Exception):
    pass


class ContextLoader:
    """
    初始化django的上下文
    """

    def __init__(self):
        self.loaded = False

    def load(self, overriding_settings_file: Optional[str] = None, **overriding_settings):
        """
        初始化django上下文, 可以用settings_json_file_path来初始化
        :type overriding_settings: 覆盖django全局配置的字典
        :param overriding_settings_file: Django的settings配置文件路径，使用json格式，其中的配置会覆盖haorm默认启动的django的配置
        :return:
        """
        if self.loaded:
            return

        settings_path = overriding_settings_file or os.path.join(os.path.abspath(os.getcwd()), DEFAULT_FILENAME)
        if not os.path.exists(settings_path):
            with open(settings_path, 'w', encoding='utf-8') as f:
                f.write(json.dumps(DEFAULT_SETTINGS, indent=2))

            raise HaormSettingsError('')

        override_settings = json.loads(open(settings_path, encoding='utf-8').read())
        override_settings.update(**overriding_settings)
        os.environ.setdefault('HAORM_DJANGO_SETTINGS', json.dumps(override_settings, ensure_ascii=False))

        os.environ.setdefault("DJANGO_SETTINGS_MODULE", "haorm.settings")
        django.setup()
        self.loaded = True


context_loader = ContextLoader()

if __name__ == '__main__':
    context_loader.load()
