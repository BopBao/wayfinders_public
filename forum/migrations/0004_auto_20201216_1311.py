# Generated by Django 3.1.2 on 2020-12-16 13:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('forum', '0003_auto_20201216_1309'),
    ]

    operations = [
        migrations.AlterField(
            model_name='thread',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
