# Generated by Django 4.2.7 on 2023-12-05 13:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bboard', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='bb',
            name='kind',
            field=models.CharField(choices=[('b', 'Куплю'), ('s', 'Продам'), ('c', 'обменяю')], default='s', max_length=1),
        ),
    ]
