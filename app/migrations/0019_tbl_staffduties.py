# Generated by Django 4.2.1 on 2023-10-07 10:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0018_rename_product_id_tbl_cart_brandname_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='tbl_staffDuties',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sellername', models.CharField(max_length=30)),
                ('staffname', models.CharField(max_length=30)),
                ('assigned_date', models.DateField()),
                ('instructions', models.CharField(max_length=100)),
                ('order_id', models.IntegerField()),
                ('status', models.CharField(max_length=30)),
            ],
            options={
                'db_table': 'tbl_staffDuties',
            },
        ),
    ]
