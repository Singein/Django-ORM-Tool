
class DataBaseRouter(object):
    ''' A router to control all database operations on models for different databases.
    In case an app is not set in settings.DATABASE_APPS_MAPPING,
    the router will fallback to the `default` database.
     Settings example: DATABASE_APPS_MAPPING = {'app1': 'db1', 'app2': 'db2'} '''

    def db_for_read(self, model, **hints):
        """"Point all read operations to the specific database."""
        return model._meta.app_label

    def db_for_write(self, model, **hints):
        """Point all write operations to the specific database."""
        return model._meta.app_label
