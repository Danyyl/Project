# Generated by Django 3.0.5 on 2020-06-05 16:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Server', '0010_auto_20200605_1947'),
    ]

    operations = [
        migrations.AlterField(
            model_name='session',
            name='state',
            field=models.CharField(max_length=1000),
        ),
    ]