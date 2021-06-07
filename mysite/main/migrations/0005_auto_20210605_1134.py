# Generated by Django 3.2.3 on 2021-06-05 06:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_transfers'),
    ]

    operations = [
        migrations.RenameField(
            model_name='transfers',
            old_name='cust_name',
            new_name='receiver_name',
        ),
        migrations.RemoveField(
            model_name='transfers',
            name='cust_id',
        ),
        migrations.AddField(
            model_name='transfers',
            name='credit',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='transfers',
            name='receiver_id',
            field=models.ForeignKey(default=1000, on_delete=django.db.models.deletion.CASCADE, related_name='receiver_id', to='main.customers'),
        ),
        migrations.AddField(
            model_name='transfers',
            name='sender_id',
            field=models.ForeignKey(default=1000, on_delete=django.db.models.deletion.CASCADE, related_name='sender_id', to='main.customers'),
        ),
    ]
