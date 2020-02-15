from dotlib import ORM
# ORM is a context manager, it is responsible for loading Django's
# db module according to the given database configuration information.

from dotlib import table2model
# The table2model method is responsible for converting the table with
# the specified name under the specified database connection to a django orm model


with ORM(dbconfig='./dbconfig.json'):
    # dbconfig is the path of the configuration file just created
    # deconfig's default value is the absolute path of dbconfig.json 
    # in the current directory

    # Suppose we have a table named student under the default connection
    Student = table2model('student', 'default')

    # Now you have a Django-ORM model of the student table named Student

    record = Student.objects.get(id=1)
    
    # Enjoy!

