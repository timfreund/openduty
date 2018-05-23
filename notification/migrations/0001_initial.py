# -*- coding: utf-8 -*-
from django.db import models, migrations

class Migration(migrations.Migration):
    dependencies = [
        ('openduty', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserNotificationMethod',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('user', models.ForeignKey(to='auth.User', related_name='notification_methods')),
                ('position', models.IntegerField()),
                ('method', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='ScheduledNotification',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('notifier', models.CharField(max_length=30)),
                ('message', models.CharField(max_length=500)),
                ('user_to_notify', models.ForeignKey(to='auth.User')),
                ('send_at', models.DateTimeField()),
                ('incident', models.ForeignKey(to='openduty.Incident')),
            ],
        ),
    ]

