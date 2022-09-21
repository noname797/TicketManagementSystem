# Generated by Django 3.2.15 on 2022-09-21 07:28

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('Tickets', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='subcategory',
            old_name='subCategory',
            new_name='subcategory',
        ),
        migrations.RemoveField(
            model_name='ticket',
            name='ticket_id',
        ),
        migrations.AddField(
            model_name='subcategory',
            name='category',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='category_sub', to='Tickets.category'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='ticket',
            name='id',
            field=models.BigAutoField(auto_created=True, default=0, primary_key=True, serialize=False, verbose_name='ID'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='ticket',
            name='issue_date',
            field=models.DateField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]