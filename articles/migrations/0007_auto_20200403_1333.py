# Generated by Django 2.2.10 on 2020-04-03 08:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0006_auto_20200403_1331'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='mode',
            field=models.CharField(choices=[(1, 'Online Event'), (2, 'Offline Mode')], default=1, max_length=10),
        ),
    ]