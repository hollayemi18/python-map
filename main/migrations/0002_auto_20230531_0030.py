# Generated by Django 3.2.2 on 2023-05-30 23:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('street', models.CharField(max_length=300)),
                ('city', models.CharField(max_length=300)),
                ('country', models.CharField(max_length=300)),
            ],
        ),
        migrations.DeleteModel(
            name='Data',
        ),
    ]