# Generated by Django 3.1.5 on 2021-04-11 06:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('to', models.CharField(max_length=30)),
                ('From', models.CharField(max_length=30)),
                ('amount', models.PositiveIntegerField()),
                ('status', models.CharField(max_length=20)),
                ('t_id', models.PositiveIntegerField()),
                ('time', models.DateTimeField()),
            ],
        ),
    ]
