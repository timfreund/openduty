# -*- coding: utf-8 -*-
from django.db import models, migrations


class Migration(migrations.Migration):
    dependencies = [
        ('openduty', '0006_load_default_data')
    ]

    operations = [
        migrations.AddField('Service', 'notifications_disabled',
                            models.BooleanField(default=False)),
    ]
    
