# Generated by Django 3.1.2 on 2021-01-24 17:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0008_company_main_image'),
        ('cal', '0002_auto_20210124_1712'),
    ]

    operations = [
        migrations.AddField(
            model_name='calendar',
            name='company',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='members.company'),
        ),
        migrations.AddField(
            model_name='calendar',
            name='member',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='members.member'),
        ),
    ]
