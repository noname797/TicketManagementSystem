# Generated by Django 3.2.15 on 2022-09-21 08:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Login', '0002_alter_profile_ps_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]