# Generated by Django 3.0.7 on 2020-06-15 11:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CurriculumDesign', '0003_auto_20200615_1842'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stu_info',
            name='id',
            field=models.IntegerField(max_length=12, primary_key=True, serialize=False),
        ),
    ]
