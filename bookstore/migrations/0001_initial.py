# Generated by Django 3.2.6 on 2023-12-21 03:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('author', models.CharField(max_length=200)),
                ('description', models.CharField(max_length=500)),
                ('price', models.FloatField(blank=True, null=True)),
                ('image', models.ImageField(upload_to='image/')),
                ('follow_author', models.TextField(blank=True, null=True)),
                ('book_available', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='CtfTaskObjects',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=100)),
                ('password', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='UserDatas',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('flag', models.CharField(max_length=100)),
                ('for_team', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='ConnectionJournal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=100)),
                ('is_connected', models.BooleanField()),
                ('task_object', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='bookstore.ctftaskobjects')),
            ],
        ),
    ]
