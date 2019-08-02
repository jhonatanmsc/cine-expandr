# Generated by Django 2.2.4 on 2019-08-02 02:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_auto_20190802_0219'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='session',
            name='showtime',
        ),
        migrations.AddField(
            model_name='showtime',
            name='session',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='showtime', to='core.Session'),
        ),
    ]
