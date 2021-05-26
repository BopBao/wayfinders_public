# Generated by Django 3.1.2 on 2021-05-26 14:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0002_auto_20210526_1410'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='booking_interval_buffer',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='event',
            name='busy_private',
            field=models.BooleanField(default=False),
        ),
        migrations.CreateModel(
            name='GuestParticipant',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('guest_name', models.CharField(max_length=255)),
                ('guest_email', models.EmailField(max_length=255)),
                ('events', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='events.event')),
            ],
            options={
                'verbose_name': 'Guest Participant',
                'verbose_name_plural': 'Guest Participants',
            },
        ),
    ]
