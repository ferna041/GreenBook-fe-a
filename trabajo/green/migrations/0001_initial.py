# Generated by Django 3.2.9 on 2021-12-01 02:51

from django.db import migrations, models
import django.utils.timezone
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('identifier', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('slug', models.SlugField(max_length=20)),
                ('description', models.TextField()),
                ('image', models.ImageField(default='images/Fondo.png', upload_to='images/')),
                ('published', models.DateTimeField(default=django.utils.timezone.now)),
                ('likes', models.IntegerField()),
            ],
            options={
                'ordering': ('-published',),
            },
        ),
    ]
