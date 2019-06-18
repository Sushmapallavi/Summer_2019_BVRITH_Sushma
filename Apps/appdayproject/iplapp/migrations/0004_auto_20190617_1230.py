# Generated by Django 2.2.2 on 2019-06-17 07:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('iplapp', '0003_auto_20190617_1226'),
    ]

    operations = [
        migrations.AlterField(
            model_name='matches',
            name='result',
            field=models.CharField(max_length=64, null=True),
        ),
        migrations.AlterField(
            model_name='matches',
            name='team_1',
            field=models.CharField(max_length=128, null=True),
        ),
        migrations.AlterField(
            model_name='matches',
            name='team_2',
            field=models.CharField(max_length=64, null=True),
        ),
        migrations.AlterField(
            model_name='matches',
            name='toss_decision',
            field=models.CharField(max_length=64, null=True),
        ),
        migrations.AlterField(
            model_name='matches',
            name='toss_winner',
            field=models.CharField(max_length=64, null=True),
        ),
    ]
