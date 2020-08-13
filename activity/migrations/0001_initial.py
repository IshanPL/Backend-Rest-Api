# Generated by Django 3.0 on 2020-08-13 07:10

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.SlugField(max_length=100, primary_key=True, serialize=False)),
                ('real_name', models.CharField(max_length=100)),
                ('tz', models.CharField(choices=[('Asia', 'Asia'), ('America/Los_Angeles', 'America/Los_Angeles')], default='Asia', max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Activity',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_time', models.DateTimeField(default=django.utils.timezone.now)),
                ('end_time', models.DateTimeField()),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='activity.User')),
            ],
        ),
    ]