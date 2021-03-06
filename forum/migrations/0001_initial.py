# Generated by Django 3.1.2 on 2021-05-18 17:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('members', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('body', models.TextField()),
                ('created_by_string', models.CharField(max_length=255)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('edited_at', models.DateTimeField(auto_now_add=True)),
                ('edited', models.BooleanField(default=False)),
                ('likes', models.IntegerField(default=0)),
                ('flagged', models.BooleanField(default=False)),
                ('number_of_flags', models.IntegerField(default=0)),
                ('created_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='members.memberuser')),
            ],
        ),
        migrations.CreateModel(
            name='Thread',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('subtitle', models.CharField(max_length=255)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('created_by_string', models.CharField(max_length=255)),
                ('sticky', models.BooleanField(default=False)),
                ('created_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='members.memberuser')),
            ],
            options={
                'verbose_name': 'Discussion',
                'verbose_name_plural': 'Discussions',
            },
        ),
        migrations.CreateModel(
            name='Reply',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('body', models.TextField()),
                ('created_by_string', models.CharField(max_length=255)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('edited_at', models.DateTimeField(auto_now_add=True)),
                ('edited', models.BooleanField(default=False)),
                ('likes', models.IntegerField(default=0)),
                ('flagged', models.BooleanField(default=False)),
                ('number_of_flags', models.IntegerField(default=0)),
                ('created_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='members.memberuser')),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='forum.post')),
                ('thread', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='forum.thread')),
            ],
            options={
                'verbose_name': 'Reply',
                'verbose_name_plural': 'Replies',
            },
        ),
        migrations.AddField(
            model_name='post',
            name='thread',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='forum.thread'),
        ),
        migrations.CreateModel(
            name='MemberLikeOrFlagReply',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('flagged', models.BooleanField(default=False)),
                ('like', models.BooleanField(default=False)),
                ('member', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='members.memberuser')),
                ('reply', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='forum.reply')),
            ],
            options={
                'verbose_name': 'Member Likes Reply',
                'verbose_name_plural': 'Members Like Replies',
            },
        ),
        migrations.CreateModel(
            name='MemberLikeOrFlagPost',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('flagged', models.BooleanField(default=False)),
                ('like', models.BooleanField(default=False)),
                ('member', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='members.memberuser')),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='forum.post')),
            ],
            options={
                'verbose_name': 'Member Likes Post',
                'verbose_name_plural': 'Members Like Posts',
            },
        ),
    ]
