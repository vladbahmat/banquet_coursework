# Generated by Django 3.1.7 on 2021-04-28 09:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('banquet', '0005_remove_customer_birthday'),
    ]

    operations = [
        migrations.AddField(
            model_name='banquet',
            name='is_approved',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='customer',
            name='balance',
            field=models.IntegerField(default=1000),
        ),
        migrations.AlterField(
            model_name='customer',
            name='discount',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='customer',
            name='spend_money',
            field=models.IntegerField(default=0),
        ),
    ]