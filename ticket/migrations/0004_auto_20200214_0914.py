# Generated by Django 3.0.3 on 2020-02-14 09:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ticket', '0003_remove_servicerequest_waiting_for'),
    ]

    operations = [
        migrations.AlterField(
            model_name='servicerequest',
            name='description',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='description'),
        ),
        migrations.AlterField(
            model_name='servicerequest',
            name='extra',
            field=models.TextField(blank=True, null=True, verbose_name='extra'),
        ),
    ]
