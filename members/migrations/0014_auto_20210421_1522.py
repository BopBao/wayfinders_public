# Generated by Django 3.1.2 on 2021-04-21 15:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0013_company_public'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='company',
            options={'verbose_name': 'Group', 'verbose_name_plural': 'Groups'},
        ),
    ]