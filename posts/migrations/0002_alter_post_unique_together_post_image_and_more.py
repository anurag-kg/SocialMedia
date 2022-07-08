# Generated by Django 4.0.5 on 2022-07-07 19:08

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('posts', '0001_initial'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='post',
            unique_together=set(),
        ),
        migrations.AddField(
            model_name='post',
            name='image',
            field=models.ImageField(blank=True, height_field=200, upload_to='SocialMedia/photos', width_field=200),
        ),
        migrations.AlterUniqueTogether(
            name='post',
            unique_together={('user', 'message', 'image')},
        ),
    ]
