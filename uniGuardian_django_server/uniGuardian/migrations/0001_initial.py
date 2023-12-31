# Generated by Django 4.1.13 on 2023-11-29 04:39

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('email', models.CharField(max_length=155, primary_key=True, serialize=False)),
                ('createdAt', models.TimeField(auto_now_add=True)),
                ('raw_resume', models.TextField()),
                ('raw_sop', models.TextField()),
                ('raw_lor', models.TextField()),
                ('psychometrics', models.TextField(default='')),
                ('analysis', models.TextField(default='')),
            ],
        ),
    ]
