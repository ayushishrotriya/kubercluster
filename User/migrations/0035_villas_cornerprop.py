# Generated by Django 4.1.1 on 2022-10-21 17:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('User', '0034_villas_additionalroom'),
    ]

    operations = [
        migrations.AddField(
            model_name='villas',
            name='cornerprop',
            field=models.CharField(default='Yes', max_length=5),
        ),
    ]
