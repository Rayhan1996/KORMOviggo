# Generated by Django 2.2 on 2020-02-08 11:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0006_auto_20200208_0036'),
    ]

    operations = [
        migrations.AddField(
            model_name='apply',
            name='student_id',
            field=models.FileField(default='id.txt', upload_to='id'),
        ),
        migrations.AlterField(
            model_name='apply',
            name='phone',
            field=models.CharField(default='01000000000', max_length=500),
        ),
    ]