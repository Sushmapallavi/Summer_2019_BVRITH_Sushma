# Generated by Django 2.2.2 on 2019-06-06 15:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('onlineapp', '0002_student'),
    ]

    operations = [
        migrations.CreateModel(
            name='MockTest1',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('problem1', models.IntegerField()),
                ('problem2', models.IntegerField()),
                ('problem3', models.IntegerField()),
                ('problem4', models.IntegerField()),
                ('total', models.IntegerField()),
                ('student', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='onlineapp.Student')),
            ],
        ),
    ]