# Generated by Django 4.1.5 on 2023-01-16 13:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Students',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('father_name', models.CharField(max_length=200)),
                ('contact', models.CharField(max_length=200)),
                ('city', models.CharField(choices=[('PURNEA', 'PURNEA'), ('PATNA', 'PATNA'), ('BHOPAL', 'BHOPAL'), ('Ranchi', 'Ranchi')], max_length=200)),
            ],
        ),
    ]
