# Generated by Django 3.1.2 on 2021-05-25 23:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0004_auto_20210519_0352'),
    ]

    operations = [
        migrations.AddField(
            model_name='memberuser',
            name='is_wf_admin',
            field=models.BooleanField(default=False),
        ),
    ]
