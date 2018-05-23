# -*- coding: utf-8 -*-
from django.db import models, migrations


class Migration(migrations.Migration):
    dependencies = [
        ('openduty', '0008_auto__add_servicesilenced'),
    ]

    operations = [
        migrations.CreateModel(
            name='IncidentSilenced',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('incident', models.ForeignKey(to='openduty.incident')),
                ('silenced', models.BooleanField(default=False)),
                ('silenced_until', models.DateTimeField()),
            ]
        )
    ]
 
