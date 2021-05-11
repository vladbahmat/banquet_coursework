# Generated by Django 3.1.6 on 2021-02-10 20:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Drink',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Food',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Music',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('genre', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('login', models.CharField(max_length=30)),
                ('password', models.CharField(max_length=40)),
            ],
        ),
        migrations.CreateModel(
            name='Banquet',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('money', models.IntegerField()),
                ('people', models.IntegerField()),
                ('drink', models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='banquet.drink')),
                ('food', models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='banquet.food')),
                ('music', models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='banquet.music')),
                ('user', models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='banquet.user')),
            ],
        ),
    ]
