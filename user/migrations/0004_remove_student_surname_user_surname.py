# Generated by Django 4.1.2 on 2022-10-27 11:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0003_teacher'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student',
            name='surname',
        ),
        migrations.AddField(
            model_name='user',
            name='surname',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
