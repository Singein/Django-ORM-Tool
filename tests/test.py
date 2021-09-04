# from django.db import models
# from loguru import logger
#
# from dotlib import MetaReflex
# from dotlib import ORM
#
# # ORM is a context manager, it is responsible for loading Django's
# # db module according to the given database configuration information.
# # The table2model method is responsible for converting the table with
# # the specified name under the specified database connection to a django orm model
#
#
# # logger.add(sys.stdout, level="INFO", filter=__file__)
# with ORM():
#     pass
#
#
# class TestModel(models.Model):
#     def save(self):
#         print('test model print')
#         super().save()
#
#     class Meta:
#         abstract = True
#
#
# class TestModel2(models.Model):
#     def save(self):
#         print('test model2 print')
#         super().save()
#
#     class Meta:
#         abstract = True
#
#
# if __name__ == '__main__':
#     MODEL = MetaReflex.table2model('blogs_article', 'default', TestModel)
#     MODEL2 = MetaReflex.table2model('student', 'test')
#     student = MODEL2.objects.get(id=1)
#     logger.info(student.class_field.name)
#     logger.info(student.class_field.school.name)
#     logger.info(student.class_field)
#
# # with ORM(dbconfig='./dbconfig.json'):
# #     # dbconfig is the path of the configuration file just created
# #     # deconfig's default value is the absolute path of dbconfig.json
# #     # in the current directory
#
# #     # Suppose we have a table named student under the default connection
# #     Student = table2model('student', 'default')
#
# #     # Now you have a Django-ORM model of the student table named Student
#
# #     record = Student.objects.get(id=1)
#
# #     # Enjoy!
