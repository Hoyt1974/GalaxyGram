# Generated by Django 3.2.5 on 2021-07-21 21:39

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Planet_Comments',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.CharField(max_length=140)),
                ('creation_time', models.DateTimeField(default=django.utils.timezone.now)),
                ('up_vote', models.IntegerField(default=0)),
                ('down_vote', models.IntegerField(default=0)),
                ('total_votes', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Planet_Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('planet_name', models.CharField(max_length=200)),
                ('planet_img', models.ImageField(upload_to='images/')),
                ('post', models.CharField(max_length=140)),
                ('creation_time', models.DateTimeField(default=django.utils.timezone.now)),
                ('up_vote', models.IntegerField(default=0)),
                ('down_vote', models.IntegerField(default=0)),
                ('total_votes', models.IntegerField(default=0)),
            ],
        ),
    ]
