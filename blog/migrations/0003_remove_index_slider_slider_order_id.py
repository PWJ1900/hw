# Generated by Django 2.2.14 on 2020-07-30 09:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_index_slider'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='index_slider',
            name='slider_order_id',
        ),
    ]
