# Generated by Django 3.0.7 on 2020-06-17 08:37

from django.db import migrations, models
import django.db.models.manager


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Stu_Info',
            fields=[
                ('id', models.CharField(max_length=16, primary_key=True, serialize=False)),
                ('max_count', models.IntegerField(default=3)),
                ('is_same', models.BooleanField(default=False)),
            ],
            managers=[
                ('object', django.db.models.manager.Manager()),
            ],
        ),
    ]