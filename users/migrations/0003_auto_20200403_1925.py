# Generated by Django 2.2.10 on 2020-04-03 13:55

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_auto_20200403_1507'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='contact_number',
            field=models.CharField(default='**********', max_length=10, validators=[django.core.validators.RegexValidator(code='nomatch', message='Enter a 10 digit mobile number', regex='^.{10}$')]),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='email',
            field=models.CharField(default='xyz@gmail.com', max_length=50),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='whatsapp_number',
            field=models.CharField(default='**********', max_length=10, validators=[django.core.validators.RegexValidator(code='nomatch', message='Enter a 10 digit mobile number', regex='^.{10}$')]),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='position',
            field=models.IntegerField(choices=[(0, 'Choose an option'), (1, 'Technical Head ACM'), (2, 'Technical Head ACM-W'), (3, 'Webmaster ACM'), (4, 'Webmaster ACM-W'), (5, 'Events Head ACM'), (6, 'Events Head ACM-W'), (7, 'PR Head ACM'), (8, 'PR Head ACM-W'), (9, 'Design Head ACM'), (10, 'Design Head ACM-W'), (11, 'Editorial Head ACM'), (12, 'Editorial Head ACM-W')], default=0),
        ),
    ]
