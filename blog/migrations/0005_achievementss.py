# Generated by Django 2.2.14 on 2020-08-04 12:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_index_introduction_index_people'),
    ]

    operations = [
        migrations.CreateModel(
            name='Achievementss',
            fields=[
                ('ID', models.AutoField(primary_key=True, serialize=False)),
                ('orderID', models.IntegerField(null=True)),
                ('paperinfo', models.TextField()),
                ('index', models.CharField(max_length=400, null=True)),
                ('pdf_link', models.CharField(max_length=1000)),
                ('index_link', models.CharField(max_length=1000, null=True)),
            ],
        ),
    ]
