# -*- coding: utf-8 -*-
from django.contrib.auth import models as auth_models
from django.core.management import call_command

from django.db import models, migrations

def add_root_user(apps, schema_editor):
    print '*' * 80
    print 'Skipping root user creation'
    print '*' * 80
    # try:
    #     auth_models.User.objects.get(username='root')
    # except auth_models.User.DoesNotExist:
    #     print '*' * 80
    #     print 'Creating root user -- login: root, password: toor'
    #     print '*' * 80
    #     assert auth_models.User.objects.create_superuser('root', 'admin@localhost', 'toor')
    # else:
    #     print 'Test user already exists.'

class Migration(migrations.Migration):
    dependencies = [
        ("openduty", "0005_auto__add_field_userprofile_prowl_api_key__add_field_userprofile_prowl"),
    ]

    operations = [
        migrations.RunPython(add_root_user),
    ]
    
