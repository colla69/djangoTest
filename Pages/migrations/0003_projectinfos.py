# Generated by Django 2.1.7 on 2019-03-12 18:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Pages', '0002_auto_20190312_1618'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProjectInfos',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_column='Name', max_length=100)),
                ('start_date', models.DateField(blank=True, null=True)),
                ('end_date', models.DateField(blank=True, null=True)),
                ('description', models.CharField(blank=True, max_length=4000, null=True)),
                ('role_name', models.CharField(blank=True, max_length=50, null=True)),
                ('lang', models.CharField(blank=True, max_length=100, null=True)),
                ('company', models.CharField(blank=True, max_length=200, null=True)),
            ],
            options={
                'db_table': 'project_infos',
                'managed': False,
            },
        ),
    ]
