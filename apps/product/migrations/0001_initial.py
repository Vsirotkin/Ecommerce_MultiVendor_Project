# Generated by Django 4.1.3 on 2022-11-28 08:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('slug', models.SlugField(max_length=100)),
                ('ordering', models.IntegerField(default=0)),
            ],
            options={
                'verbose_name_plural': 'categories',
                'ordering': ['ordering'],
            },
        ),
    ]
