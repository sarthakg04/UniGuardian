# Generated by Django 4.1.13 on 2023-11-29 04:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('uniGuardian', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='raw_lor',
        ),
        migrations.AddField(
            model_name='userprofile',
            name='raw_lor1',
            field=models.TextField(default=''),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='raw_lor2',
            field=models.TextField(default=''),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='raw_resume',
            field=models.TextField(default=''),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='raw_sop',
            field=models.TextField(default=''),
        ),
    ]
