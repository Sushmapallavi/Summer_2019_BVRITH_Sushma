# Generated by Django 2.2.2 on 2019-06-09 00:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todoapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todoitem',
            name='due_date',
            field=models.DateField(blank=True, null=True),
        ),
    ]
