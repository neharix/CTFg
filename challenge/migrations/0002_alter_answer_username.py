# Generated by Django 5.0 on 2024-09-29 12:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('challenge', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='answer',
            name='username',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
