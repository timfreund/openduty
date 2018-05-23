# -*- coding: utf-8 -*-
from django.db import models, migrations


class Migration(migrations.Migration):
    dependencies = [
        ('openduty', '0002_auto_20150804_1449'),
    ]

    operations = [
        migrations.AlterField('Incident', 'incident_key', models.CharField(max_length=200)),
    ]

