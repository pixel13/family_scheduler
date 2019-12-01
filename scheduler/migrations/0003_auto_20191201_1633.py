# Generated by Django 2.2.6 on 2019-12-01 15:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scheduler', '0002_auto_20191113_2309'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'ordering': ['name'], 'verbose_name_plural': 'categories'},
        ),
        migrations.AlterModelOptions(
            name='item',
            options={'ordering': ['day', 'start', 'order']},
        ),
        migrations.AlterModelOptions(
            name='schedule',
            options={'ordering': ['order']},
        ),
        migrations.AlterField(
            model_name='category',
            name='data_args',
            field=models.TextField(blank=True, help_text='Arguments (depending on data_type)', null=True),
        ),
        migrations.AlterField(
            model_name='category',
            name='data_type',
            field=models.CharField(choices=[('events', 'events - A list of events'), ('text', 'text - Free text'), ('checkbox', 'checkbox - A boolean information (true or false)'), ('iconset', 'iconset - A choice among a list of icons'), ('select', 'select - A select box'), ('open_select', 'open_select - A select box that accepts (and store) new values')], max_length=30),
        ),
    ]
