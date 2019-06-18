# Generated by Django 2.2.2 on 2019-06-17 12:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('iplapp', '0006_matches_match_id'),
    ]

    operations = [
        migrations.RenameField(
            model_name='deliveries',
            old_name='leg_bye_runs',
            new_name='legbye_runs',
        ),
        migrations.RemoveField(
            model_name='deliveries',
            name='is_superover',
        ),
        migrations.RemoveField(
            model_name='matches',
            name='match_id',
        ),
        migrations.AddField(
            model_name='deliveries',
            name='is_super_over',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='deliveries',
            name='batsman',
            field=models.CharField(max_length=64, null=True),
        ),
        migrations.AlterField(
            model_name='deliveries',
            name='batting_team',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='deliveries',
            name='bowler',
            field=models.CharField(max_length=64, null=True),
        ),
        migrations.AlterField(
            model_name='deliveries',
            name='bowling_team',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='deliveries',
            name='dismissal_kind',
            field=models.CharField(max_length=64, null=True),
        ),
        migrations.AlterField(
            model_name='deliveries',
            name='fielder',
            field=models.CharField(max_length=64, null=True),
        ),
        migrations.AlterField(
            model_name='deliveries',
            name='non_striker',
            field=models.CharField(max_length=64, null=True),
        ),
        migrations.AlterField(
            model_name='deliveries',
            name='player_dismissed',
            field=models.CharField(max_length=64, null=True),
        ),
        migrations.AlterField(
            model_name='matches',
            name='id',
            field=models.IntegerField(default=-1, primary_key=True, serialize=False),
        ),
    ]
