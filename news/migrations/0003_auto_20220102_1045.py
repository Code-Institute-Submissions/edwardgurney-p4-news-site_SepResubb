# Generated by Django 3.2 on 2022-01-02 10:45

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('news', '0002_post_content'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='comment',
            options={'ordering': ['created_on']},
        ),
        migrations.AddField(
            model_name='comment',
            name='inappropriate_post',
            field=models.ManyToManyField(blank=True, related_name='inappropriate_posts', to=settings.AUTH_USER_MODEL),
        ),
    ]