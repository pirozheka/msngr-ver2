# Generated by Django 5.1.1 on 2024-09-26 07:21

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='ChatRoom',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('is_group', models.BooleanField(default=False)),
                ('members', models.ManyToManyField(blank=True, related_name='chat_members', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
