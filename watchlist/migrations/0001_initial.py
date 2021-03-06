# Generated by Django 2.0.3 on 2019-07-09 13:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Watchlist',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content_id', models.PositiveIntegerField()),
                ('title', models.CharField(max_length=100)),
                ('type', models.CharField(max_length=6)),
                ('date', models.DateField(auto_now_add=True)),
                ('watched', models.BooleanField(default=False)),
            ],
        ),
    ]
