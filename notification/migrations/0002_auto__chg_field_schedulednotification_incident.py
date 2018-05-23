# -*- coding: utf-8 -*-
from django.db import models, migrations


class Migration(migrations.Migration):
    dependencies = [
        ('notification', '0001_initial'),
    ]

    operations = [
        migrations.AlterField('ScheduledNotification', 'incident_id', models.ForeignKey(to='openduty.Incident', null=True)),
    ]
    
