# Generated by Django 4.1.1 on 2022-10-21 18:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('User', '0037_house_image1_house_image2_house_image3'),
    ]

    operations = [
        migrations.AddField(
            model_name='house',
            name='additionalroom',
            field=models.CharField(default='Room', max_length=50),
        ),
        migrations.AddField(
            model_name='house',
            name='cornerprop',
            field=models.CharField(default='NO', max_length=5),
        ),
        migrations.AddField(
            model_name='house',
            name='rate',
            field=models.CharField(default='54216', max_length=50),
        ),
        migrations.AddField(
            model_name='house',
            name='tokenamount',
            field=models.CharField(default='500000', max_length=50),
        ),
        migrations.AlterField(
            model_name='apartments',
            name='rate',
            field=models.CharField(default='54216', max_length=50),
        ),
    ]
