# Generated by Django 3.0.6 on 2020-06-18 15:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_auto_20200618_2054'),
    ]

    operations = [
        migrations.AlterField(
            model_name='addstudent',
            name='past_Experience',
            field=models.TextField(max_length=256),
        ),
    ]