# -*- coding: utf-8 -*-
from django.db import models, migrations


class Migration(migrations.Migration):
    dependencies = [
        ('openduty', '0004_auto__chg_field_incident_description'),
    ]

    operations = [
        migrations.AddField('userprofile', 'prowl_api_key', models.CharField(default='',
                                                                             max_length=50,
                                                                             blank=True)),
        migrations.AddField('userprofile', 'prowl_application', models.CharField(default='',
                                                                                 max_length=256,
                                                                                 blank=True)),
        migrations.AddField('userprofile', 'prowl_url', models.CharField(default='',
                                                                         max_length=512,
                                                                         blank=True)),
    ]

