# Django-ORM-Tool

A tool that can dynamically create Django orm models based on database table structure.
一个可以根据表结构动态创建Django orm 模型的工具。


## install
```shell
pip install dotlib
```

## Quick Start
First you need to create a configuration file that describes the database connection information.
We can quickly generate a template in the current directory through the `dotlib` cli-command:
```shell
dotlib
```
After running the command you will see a file named
`dbconfig.json` configuration file, the default content is as follows:
```json
{
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": "xxx",
        "USER": "postgres",
        "PASSWORD": "",
        "HOST": "",
        "PORT": ""
    }
}
```
It is not difficult to find that the configuration file just converts the django dictionary to json format.

Once configured, you are now ready to use:
```python
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

```



