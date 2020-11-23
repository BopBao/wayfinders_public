# Generated by Django 3.1.2 on 2020-11-17 22:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0003_auto_20201117_2227'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gallery',
            name='image',
            field=models.ImageField(upload_to='members/static/members/gallery/'),
        ),
        migrations.AlterField(
            model_name='member',
            name='main_image',
            field=models.ImageField(blank=True, upload_to='members/static/members/profile_pic/'),
        ),
    ]