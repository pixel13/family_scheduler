# Generated by Django 2.2.6 on 2019-12-01 15:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scheduler', '0004_auto_20191201_1639'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='order',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]