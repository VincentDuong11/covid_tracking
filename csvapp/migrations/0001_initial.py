# Generated by Django 2.2.18 on 2021-02-05 21:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Record',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pruid', models.IntegerField()),
                ('prname', models.CharField(max_length=150)),
                ('prnameFR', models.CharField(max_length=150)),
                ('date', models.DateTimeField()),
                ('numconf', models.IntegerField()),
                ('numprob', models.IntegerField()),
                ('numdeaths', models.IntegerField()),
                ('numtotal', models.IntegerField()),
                ('numtoday', models.IntegerField()),
                ('ratetotal', models.FloatField()),
            ],
        ),
    ]
