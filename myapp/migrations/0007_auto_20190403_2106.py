# Generated by Django 2.1.4 on 2019-04-03 15:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0006_auto_20190402_2051'),
    ]

    operations = [
        migrations.AlterField(
            model_name='board',
            name='name',
            field=models.CharField(max_length=30, unique=True),
        ),
    ]
