# Generated by Django 3.0.6 on 2020-06-18 15:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='addstudent',
            name='course',
        ),
        migrations.AddField(
            model_name='addstudent',
            name='email_id',
            field=models.EmailField(max_length=254, null=True),
        ),
    ]