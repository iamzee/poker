# Generated by Django 3.2.7 on 2021-09-29 05:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('oneauth', '0002_user_oneauth_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='first_name',
            field=models.CharField(blank=True, max_length=150, verbose_name='first name'),
        ),
    ]