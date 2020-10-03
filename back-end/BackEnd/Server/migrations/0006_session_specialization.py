# Generated by Django 3.0.5 on 2020-06-02 14:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Server', '0005_specialization'),
    ]

    operations = [
        migrations.AddField(
            model_name='session',
            name='specialization',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Server.Specialization'),
            preserve_default=False,
        ),
    ]
