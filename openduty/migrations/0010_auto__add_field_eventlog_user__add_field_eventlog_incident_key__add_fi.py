# -*- coding: utf-8 -*-
from django.db import models, migrations


class Migration(migrations.Migration):
    dependencies = [
        ('openduty', '0009_auto__add_incidentsilenced'),
    ]

    operations = [
        migrations.AddField(model_name='eventlog', name='user',
                            field=models.ForeignKey(to='auth.User',
                                                    default=None,
                                                    related_name='users',
                                                    null=True,
                                                    blank=True)),
    ]
