# Generated by Django 4.1.2 on 2022-10-14 16:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ongoingfront', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='usuario',
            name='senha',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
    ]