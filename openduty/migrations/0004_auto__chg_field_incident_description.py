# -*- coding: utf-8 -*-
from django.db import models, migrations


class Migration(migrations.Migration):
    dependencies = [
        ('openduty', '0003_auto__chg_field_incident_incident_key'),
    ]

    operations = [
        migrations.AlterField('Incident', 'description', models.CharField(max_length=200)),
    ]
