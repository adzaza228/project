# Generated by Django 3.1.2 on 2020-11-07 17:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_auto_20200918_1539'),
    ]

    operations = [
        migrations.CreateModel(
            name='block',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('image', models.ImageField(upload_to='')),
            ],
        ),
    ]
