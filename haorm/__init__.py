__version__ = "0.0.8"

from django.db import models

from haorm.core import Haorm


class HaormFactory:
    _MODELS_MAP = {}

    @classmethod
    def table_to_model(cls, table_name, db_alias: str = 'default', super_class: type = models.Model):
        label = f'{db_alias}.{table_name}.{super_class.__name__}'

        if label in cls._MODELS_MAP:
            return cls._MODELS_MAP.get(label, None)

        haorm = Haorm()
        cls._MODELS_MAP[label] = haorm
        return haorm


__all__ = [
    'HaormFactory'
]
