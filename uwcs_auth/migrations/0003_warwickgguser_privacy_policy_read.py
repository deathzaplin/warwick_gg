# Generated by Django 2.0.2 on 2018-06-09 07:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('uwcs_auth', '0002_auto_20180604_0822'),
    ]

    operations = [
        migrations.AddField(
            model_name='warwickgguser',
            name='privacy_policy_read',
            field=models.BooleanField(default=True),
            preserve_default=False,
        ),
    ]
