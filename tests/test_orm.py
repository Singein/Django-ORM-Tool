import os
import sys

print(os.getcwd())
sys.path.append(os.getcwd())
from dotlib import ORM, MetaReflex


def test_orm():
    with ORM():
        student = MetaReflex.table2model("student", "default")
        a = student.objects.all()[0]
        print(a.name)
        print(a.class_field.name)
        print(a.class_field.school.name)
        assert student.objects.all() > 0
        assert student.objects.all()[0]


test_orm()
