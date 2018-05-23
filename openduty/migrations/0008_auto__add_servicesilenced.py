# -*- coding: utf-8 -*-
from django.db import models, migrations


class Migration(migrations.Migration):
    dependencies = [
        ('openduty', '0007_auto__add_field_service_notifications_disabled'),
    ]

    operations = [
        migrations.CreateModel(
            name='ServiceSilenced',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('service', models.ForeignKey(to='openduty.service')),
                ('silenced', models.BooleanField(default=False)),
                ('silenced_until', models.DateTimeField()),
            ]
        )
    ]
