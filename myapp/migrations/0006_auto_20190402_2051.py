# Generated by Django 2.1.4 on 2019-04-02 15:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0005_auto_20190324_2252'),
    ]

    operations = [
        migrations.RenameField(
            model_name='board',
            old_name='title',
            new_name='name',
        ),
    ]
