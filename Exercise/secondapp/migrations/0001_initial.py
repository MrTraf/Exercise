# Generated by Django 4.1.7 on 2023-03-27 03:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='exersice_sec',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('wws_name', models.CharField(max_length=100)),
                ('wws_reps', models.CharField(max_length=20)),
                ('wws_weight', models.CharField(max_length=20)),
            ],
            options={
                'db_table': 'exersice_sec',
            },
        ),
    ]
