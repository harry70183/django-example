# Generated by Django 3.2.6 on 2021-09-03 07:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ashinne', '0002_alter_mission_product_type'),
    ]

    operations = [
        migrations.CreateModel(
            name='Login',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('account', models.CharField(max_length=40)),
                ('password', models.CharField(max_length=20)),
            ],
        ),
    ]
