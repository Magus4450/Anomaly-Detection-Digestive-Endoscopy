# Generated by Django 4.1.5 on 2023-04-08 12:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_patientinfo_other_details'),
    ]

    operations = [
        migrations.RenameField(
            model_name='patientinfo',
            old_name='first_name',
            new_name='name',
        ),
        migrations.RemoveField(
            model_name='patientinfo',
            name='last_name',
        ),
        migrations.RemoveField(
            model_name='patientinfo',
            name='other_details',
        ),
        migrations.AddField(
            model_name='patientinfo',
            name='detail',
            field=models.CharField(default=' ', max_length=200),
            preserve_default=False,
        ),
    ]
