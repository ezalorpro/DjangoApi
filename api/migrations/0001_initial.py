# Generated by Django 3.2.4 on 2021-06-14 17:57

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Todo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('name', models.CharField(blank=True, default='', max_length=255)),
                ('description', models.TextField()),
                ('status', models.BooleanField(default=False)),
            ],
            options={
                'ordering': ['created'],
            },
        ),
    ]
