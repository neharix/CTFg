# Generated by Django 3.2.6 on 2023-12-21 03:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Answer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(blank=True, max_length=20, null=True)),
                ('team', models.CharField(blank=True, max_length=20, null=True)),
                ('challenge_id', models.IntegerField()),
                ('quizz_id', models.IntegerField()),
                ('answer', models.TextField()),
                ('point', models.IntegerField()),
                ('status', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Challenge',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('owner', models.CharField(max_length=200)),
                ('public', models.BooleanField(default=False)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('date_start', models.DateTimeField()),
                ('date_end', models.DateTimeField()),
                ('description', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Hint',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quizz_id', models.IntegerField()),
                ('content', models.TextField()),
                ('point', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Quizz',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('challenge_id', models.IntegerField()),
                ('name', models.CharField(blank=True, max_length=200, null=True)),
                ('question', models.TextField()),
                ('point', models.IntegerField()),
                ('file_content', models.FileField(blank=True, null=True, upload_to='files/')),
                ('url', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='TrueAnswers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_public', models.BooleanField(default=False)),
                ('answer', models.CharField(max_length=200)),
                ('for_team', models.CharField(blank=True, max_length=100, null=True)),
                ('quizz_id', models.IntegerField()),
            ],
        ),
    ]
