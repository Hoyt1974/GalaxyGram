# Generated by Django 3.2.5 on 2021-07-19 00:20

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('planetmodel', '0001_initial'),
        ('planetpost', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='planet_post',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='planet_post',
            name='body',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='posts', to='planetmodel.body'),
        ),
        migrations.AddField(
            model_name='planet_comments',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='planet_comments',
            name='post',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='planetpost.planet_post'),
        ),
    ]
