# Generated by Django 3.0.3 on 2020-02-13 10:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ticket', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='servicerequest',
            name='duedate',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
