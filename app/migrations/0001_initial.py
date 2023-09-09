# Generated by Django 4.2.1 on 2023-09-08 04:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='tbl_userAccount',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=30)),
                ('firstname', models.CharField(max_length=30)),
                ('email', models.CharField(max_length=30)),
                ('phone', models.IntegerField()),
                ('accountType', models.CharField(max_length=30)),
            ],
            options={
                'db_table': 'tbl_userAccount',
            },
        ),
        migrations.CreateModel(
            name='tbl_userDetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=30)),
                ('firstname', models.CharField(max_length=30)),
                ('lastname', models.CharField(max_length=30)),
                ('gender', models.CharField(max_length=30)),
                ('email', models.CharField(max_length=30)),
                ('phone', models.IntegerField()),
                ('address', models.CharField(max_length=50)),
                ('district', models.CharField(max_length=30)),
                ('photo', models.CharField(max_length=50)),
            ],
            options={
                'db_table': 'tbl_userDetails',
            },
        ),
    ]