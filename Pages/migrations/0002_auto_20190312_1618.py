# Generated by Django 2.1.7 on 2019-03-12 16:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Pages', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='store',
            name='title',
            field=models.TextField(default='cool shit'),
        ),
    ]