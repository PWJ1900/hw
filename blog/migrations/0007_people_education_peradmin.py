# Generated by Django 3.1.1 on 2020-10-18 09:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_auto_20200807_1342'),
    ]

    operations = [
        migrations.CreateModel(
            name='people_education',
            fields=[
                ('id', models.IntegerField(max_length=100, primary_key=True, serialize=False)),
                ('time', models.CharField(max_length=400)),
                ('education', models.CharField(max_length=400)),
                ('university', models.CharField(max_length=400)),
            ],
        ),
        migrations.CreateModel(
            name='Peradmin',
            fields=[
                ('article_id', models.AutoField(primary_key=True, serialize=False)),
                ('number', models.TextField()),
                ('passoword', models.TextField()),
                ('name', models.TextField()),
            ],
        ),
    ]
